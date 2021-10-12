# stu_num: 2035060829


# 检验是否为合法矩阵
def check_mat(mat, row):
    check_shape = set()
    for i in range(row):
        check_shape.add(len(mat[i]))
    if len(check_shape) != 1:
        return 0
    return 1


def mat_mul(mat_a, mat_b):
    shape_a = (len(mat_a), len(mat_a[0]))
    shape_b = (len(mat_b), len(mat_b[0]))
    # 1. 检验是否为矩阵
    if (0 == check_mat(mat_a, shape_a[0])) or (0 == check_mat(mat_b, shape_a[0])):
        print("所用来计算的矩阵并非都是是矩阵！\n")
        return

    # 2. 检验矩阵是否可以相乘

    # print(shape_a)
    # print(shape_b)
    if shape_a[1] != shape_b[0]:
        return f"所输入的矩阵不符合规范！\n"

    # 3. 计算结果
    # 构造结果矩阵
    result = [[0] * shape_b[1] for i in range(shape_a[0])]
    for i in range(shape_a[0]):
        for j in range(shape_b[1]):
            for k in range(shape_b[0]):
                result[i][j] += mat_a[i][k] * mat_b[k][j]
    return result
    # return np.matmul(np.array(mat_a), np.array(mat_b))  # -> import numpy as np


if __name__ == '__main__':
    # (3,4) · （4，2） -> (3,2)
    mat_a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
    mat_b = [[1, 2], [2, 3], [3, 4], [4, 5]]
    result = mat_mul(mat_a, mat_b)
    print(result)

# [[30, 40], [40, 54], [50, 68]]

# [[30 40]
#  [40 54]
#  [50 68]]

