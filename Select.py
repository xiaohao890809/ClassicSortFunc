# 选择排序法
def SelectSorted(nums):
    for i in range(len(nums)-1):
        minIndex = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[minIndex]:
                minIndex = j
        nums[i],nums[minIndex] = nums[minIndex],nums[i]
    return nums

nums_test = [3, 4, 1, 2, 5, 8, 0]
print(SelectSorted(nums_test))