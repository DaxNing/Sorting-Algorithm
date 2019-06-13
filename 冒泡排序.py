#!/user/bin/python
# _*_ coding: UTF-8 _*_

nums=[1,2,3,4,6,5,7,9,8,0]
n=len(nums)

def BubbleSort(nums,n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                t = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = t
    return nums

BubbleSort(nums,n)
print nums
