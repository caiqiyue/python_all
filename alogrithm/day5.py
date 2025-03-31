"""
螺旋曲线
"""
def spiral_matrix(n):
    nums = [[0 for _ in range(n)] for _ in range(n)]
    count = 1
    start_i = 0
    start_j = 0
    offset = 1
    matrix_round = 1
    while matrix_round <= int(n / 2):
        #处理上边
        for j in range(start_j,n-offset):
            nums[start_i][j] = count
            count += 1
        j += 1
        #处理右边
        for i in range(start_i,n-offset):
            nums[i][j] = count
            count += 1
        i += 1
        #处理下边
        for j in range(n-offset,start_j,-1):
            nums[i][j] = count
            count += 1
        j -= 1
        #处理左边
        for i in range(n-offset,start_i,-1):
            nums[i][j] = count
            count += 1
        i -= 1
        #进入下轮循环做准备
        start_i += 1
        start_j += 1
        offset += 1
        matrix_round += 1
    if n % 2 != 0:
        nums[start_i][start_j] = count
    return nums


if __name__ == '__main__':
    n = spiral_matrix(5)
    print(n)