#!/user/bin/python
# _*_ coding: UTF-8 _*_

nums=[1,2,3,4,6,5,7,9,8,0]
n=len(nums)

def SelectionSort(nums,n):
    for i in range(n-1):
        k=i
        for j in range(i+1,n):
            if nums[k]>nums[j]:
                k=j
        t=nums[i]
        nums[i]=nums[k]
        nums[k]=t
    return nums

SelectionSort(nums,n)
print nums