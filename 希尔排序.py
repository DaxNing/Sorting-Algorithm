#!/user/bin/python
# _*_ coding: UTF-8 _*_

nums=[1,2,4,3,5,6,7,9,8,0]
def ShellSort(arr):
    gap = l = len(arr)
    while(gap >= 1):
        gap = gap/2  #效率最高的Gap数组为为互质的数，且Gap最后要为1
        for i in xrange(0, l):
            for j in xrange(i, l - gap, gap):
                if arr[j] > arr[j+gap]:
                    arr[j], arr[j+gap] = arr[j+gap], arr[j]
    return arr

ShellSort(nums)

print nums