"""
求两个集合的交集
"""

def intersectionUseSet(num1,num2):
    result = []
    inetersection_set = set()
    for str1 in num1:
        inetersection_set.add(str1)
    for str2 in num2:
        if str2 in inetersection_set and str2 not in result:
            result.append(str2)
    return result



def intersectionUseArray(num1,num2):
    """
    给一些限制，每个字符串，由26个小写字母构成
    """
    result = []
    hash_array = [0 for _ in range(26)]
    for str1 in num1:
        if hash_array[ord(str1) - ord('a')] == 0:
            hash_array[ord(str1) - ord('a')] = 1
    for str2 in num2:
        if hash_array[ord(str2) - ord('a')] == 1:
            result.append(str2)
    return result



if __name__ == '__main__':
    rs = intersectionUseArray('abbc','cdddae')
    print(rs)

