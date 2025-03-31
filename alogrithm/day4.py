


"""
使用滑动窗口
"""

def Return_n(nums,target):
    start = 0
    sum_n = 0
    min_len = len(nums) + 1
    for end in range(len(nums)):
        sum_n += nums[end]
        while sum_n >= target:
            rs_len = end - start + 1
            sum_n -= nums[start]
            rs_len -= 1
            if rs_len <= min_len and sum_n >= target:
                min_len = rs_len
            start += 1
    if min_len > len(nums):
        return 0
    return min_len

"""
使用暴力求解法
"""

def Return(nums,target):
    min_len = len(nums) + 1
    rs_len = 0
    for i in range(len(nums)):
        sum_n = 0
        for j in range(i,len(nums)):
            sum_n += nums[j]
            if sum_n >= target:
                rs_len = j - i + 1
                break
        if min_len >= rs_len:
            min_len = rs_len
    if min_len == 0:
        return 0
    return min_len
                
        


if __name__ == '__main__':
    n = [1,4,4]
    r = Return(n,4)
    print(r)