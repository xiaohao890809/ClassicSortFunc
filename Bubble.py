# 冒泡排序法，已经归位的不用遍历
def BubbleSorted(nums):
    length = len(nums)
    for i in range(length-1):
        for j in range(length-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

nums_test = [3, 4, 1, 2, 5, 8, 0]
print(BubbleSorted(nums_test))