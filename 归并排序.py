#!/user/bin/python
# _*_ coding: UTF-8 _*_

nums=[1,2,3,4,6,5,7,9,8,0]

def Merge(nums,l,r,mid):
    te=[]
    i=l
    j=mid+1
    while i<=mid and j<=r:
        if nums[i]<nums[j]:
            te.append(nums[i])
            i+=1
        else:
            te.append(nums[j])
            j+=1
    while i<=mid:
        te.append(nums[i])
        i+=1
    while j<=r:
        te.append(nums[j])
        j+=1
    for i in range(len(te)):
        print te[i]
        nums[l+i]=te[i]
    del te



def MergeSort(nums,l,r):
    if l<r:
        mid=l+(r-l)/2
        MergeSort(nums,l,mid)
        MergeSort(nums,mid+1,r)
        Merge(nums,l,r,mid)


n=len(nums)
MergeSort(nums,0,n-1)
print nums
