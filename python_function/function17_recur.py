


def jiecheng(n):
    if n == 1:
        return 1
    return n * jiecheng(n-1)

"""
我想知道9！是多少
9！ = 9 * 8！
8！ = 8 * 7！
7！ = 7 * 6！
.......
2! = 2 * 1!
1! = 1
这叫传递，再回归
"""
print(jiecheng(3))