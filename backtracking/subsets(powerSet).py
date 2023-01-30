def subsets(nums):
    answer=[]
    def dfs(arr):
        if not arr:
            return [[]]
        num=arr.pop()
        new_arr=dfs(arr)
        copy_new_array=[]
        for item in new_arr:
            copy_new_array.append(item+[num])
        new_arr.extend(copy_new_array)
        return new_arr

    return dfs(nums)

nums = [1,2,3]
print(subsets(nums))
