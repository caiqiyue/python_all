
def isValidatedString(str1,str2):
    """
    两个字符串，都是由26个小写字母构成
    要求两个字符串的字母和各字母数量相同，但位置可以不同，称为有效字符异位词
    """
    str_matrix = [0 for i in range(26)]
    for s1 in str1:
        str_matrix[ord(s1) - ord('a')] += 1
    for s2 in str2:
        str_matrix[ord(s2) - ord('a')] -= 1
    for num in str_matrix:
        if num != 0:
            return False
    return True

if __name__ == '__main__':
    print(isValidatedString('abbca','cbab'))