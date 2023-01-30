def canFinish(numCourses, prerequisites):
    map=[i for i in range(numCourses+1)]
    def find(n):
        while(map[n]!=n):
            n=find(map[n])
        return n
    def union(p,q):
        find_p=find(p)
        find_q=find(q)
        if find_p==find_q:
            return False
        else:
            map[find_p]=find_q
    for p,q in prerequisites:
        ok=union(p,q)
        if ok==False:
            return ok
    return True
def canFinish2(numCourses, prerequisites):
    adjlist={}
    set_all = set()
    for i,j in prerequisites:
        if i in adjlist:
            adjlist[i].append(j)
        else:
            adjlist[i]=[j]
    def dfs(n):
        if n in set_all:
            return False
        if n not in adjlist:
            return True
        set_all.add(n)
        for i in adjlist[n]:
            if not dfs(i):return False
        set_all.remove(n)
        del adjlist[n]
        return True

    for i in range(numCourses+1):
        if i not in set_all:
            if not dfs(i): return False
    return True


numCourses = 3
prerequisites = [[0,1],[1,2],[2,3]]
print(canFinish2(numCourses,prerequisites))

