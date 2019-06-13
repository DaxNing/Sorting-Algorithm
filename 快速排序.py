#!/user/bin/python
# _*_ coding: UTF-8 _*_

nums=[1,2,4,3,5,6,7,9,8,0]
def Change(a,i,j):
    t=a[i]
    a[i]=a[j]
    a[j]=t
    return a

def Partiton(nums,p,q):
    i=p+1
    j=q
    x=nums[p]
    while 1:
        while i<q and nums[i]<x:
            i+=1
        while nums[j]>x:
            j-=1
        if i>=j:
            break
        Change(nums,i,j)
    Change(nums,p,j)
    return j

def QuickSort(nums,p,q):
    if p<q :
        r=Partiton(nums,p,q)
        QuickSort(nums,p,r-1)
        QuickSort(nums,r+1,q)
n=len(nums)
QuickSort(nums,0,n-1)

print nums