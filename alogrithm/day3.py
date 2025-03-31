"""
nums = [-4,-1,0,3,10]
返回有序数组的平方
"""

"""
使用双指针
"""
def square(nums):
    result = [0 for i in range(len(nums))]
    k = len(nums) - 1
    left = 0
    right = len(nums) - 1
    while left <= right:
        if (nums[left] ** 2 > nums[right] ** 2):
            result[k] = nums[left] ** 2
            left += 1
        else:
            result[k] = nums[right] ** 2
            right -= 1
        k -= 1
    return result

"""
全部平方之后，再排序
"""
def partition(nums,low,high):
    pivot = nums[low]
    while low < high:
        while low<high and nums[high] >= pivot:
            high -= 1
        nums[low] = nums[high]
        while low<high and nums[low] <= pivot:
            low += 1
        nums[high] = nums[low]
    nums[low] = pivot
    return low

def quicksort(nums,low,high):
    if low < high:
        pivot = partition(nums,low,high)
        quicksort(nums,low,pivot - 1)
        quicksort(nums,pivot + 1,high)

def square_quick_sort(nums):
    rs = [i**2 for i in nums]
    quicksort(rs,0,len(rs) - 1)
    return rs




    


        
            


if __name__ == '__main__':
    num = [-4,-1,0,3,10]
    rs = square_quick_sort(num)
    print(rs)