# 插入排序
def InsertSorted(nums):
    # 从第二元素开始直到最后一个元素
    for i in range(1,len(nums)):
        tmp = nums[i]
        print(nums)
        j = i-1
        while j>=0 and nums[j]>tmp:
            nums[j+1] = nums[j]
            j = j - 1
        nums[j+1] = tmp
    return nums

nums_test = [3, 4, 1, 2, 5, 8, 0]
print(InsertSorted(nums_test))