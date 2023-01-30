def findOrder(numCourses, prerequisites):
    adjac={}
    for i,j in prerequisites:
        if i in adjac:
            adjac[i].append(j)
        else:
            adjac[i]=[j]
    answer=[]
    visited=[False for i in range(numCourses)]
    cycle=set()
    def dfs(node):
        if node in cycle:
            return False
        if visited[node]==True:
            return
        if node not in adjac:
            visited[node] = True
            answer.append(node)
            return True
        visited[node] = True
        cycle.add(node)
        for i in adjac[node]:
            if dfs(i)==False:
                return False
        cycle.remove(node)
        answer.append(node)
        return True

    for i in range(numCourses):
        if visited[i]==False:
            if dfs(i)==False:
                return []

    return  answer

numCourses = 6
prerequisites = [[0,1],[2,0],[1,3],[3,2],[4,0],[5,0]]
print(findOrder(numCourses,prerequisites))