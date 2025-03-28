"""
移除元素
暴力求解法
"""
def Remove(nums,val):
    k = 0
    for i in range(len(nums)):
        if nums[i] == val:
            for j in range(i,len(nums) - 1):
                nums[j] = nums[j + 1]
        else:
            k += 1
    return nums[:k],k




"""
双指针法
"""
def Remove_d(nums,val):
    low = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[low] = nums[fast]
            low += 1
    return nums[:low],low


"""
计数法
"""
def Remove_c(nums,val):
    k = 0
    for i in range(len(nums)):
        if nums[i] == val:
            k += 1
        else:
            nums[i - k] = nums[i]
    return nums[:len(nums) - k],len(nums) - k




if __name__ == '__main__':
    n = [1,3,2,4,1,2,3]
    num_list,k_val = Remove_c(n,2)
    print(num_list,k_val)