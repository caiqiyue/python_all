
def search_use_while_way1(nums,target):
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2
    
    while (left <= right):
        if (nums[mid] > target):
            right = mid - 1
            
        elif (nums[mid] < target):
            left = mid + 1
            
        else:
            return mid
    return -1

def search_use_while_way2(nums,target):
    left = 0
    right = len(nums)
    mid = (left + right) // 2
    while(left < right):
        if (nums[mid] > target):
            left = mid + 1
        elif (nums[mid] < target):
            right = mid
        else:
            return mid
    return -1

def search_use_recur_way1(nums,target,left,right):
    if left <= right:
        mid = (left + right) // 2
        if (nums[mid] > target):
            return search_use_recur_way1(nums,target,left,mid - 1)
        elif (nums[mid] < target):
            return search_use_recur_way1(nums,target,mid + 1,right)
        else:
            return mid
    else:
        return -1
    

def search_use_recur_way2(nums,target,left,right):
    if left < right:
        mid = (left + right) // 2
        if (nums[mid] > target):
            return search_use_recur_way2(nums,target,left,mid)
        elif (nums[mid] < target):
            return search_use_recur_way2(nums,target,mid + 1,right)
        else:
            return mid
    else:
        return -1
    

n = [-1,0,3,5,9,12]
target = 9
rs1 = search_use_recur_way1(n,target,0,len(n) - 1)
rs2 = search_use_recur_way1(n,target,0,len(n))
print(rs1,rs2)