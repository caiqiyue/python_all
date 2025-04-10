



def twoNumberTarget(nums,target):
    searched = {}
    rs = []
    for i in range(len(nums)):
        one_rs = []
        if nums[i] not in searched.keys():
            searched[nums[i]] = i
        if (target - nums[i]) in searched.keys():
            one_rs.append(i)
            one_rs.append(searched[target - nums[i]])
            rs.append(one_rs)
    return rs



if __name__ == '__main__':
    nums = [2,7,3,6,2]
    target = 9
    
    rs = twoNumberTarget(nums,target)
    print(rs)