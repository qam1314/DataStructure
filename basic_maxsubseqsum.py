# 记录浙江大学《数据结构》中第一章的知识并实现集中最大子列和算法
'''
知识点
    一、基本概念
        1）效率与数据的组织方式相关
        2）效率与空间效率相关
        3）效率与算法的巧妙程度相关
    二、数据结构
        概念：数据在计算机中的组织方式（包括逻辑结构、存储结构）
        抽象数据结构：数据对象的描述+相关操作的描述
    三、算法
        概念：处理一个问题的流程
        关注点：1）空间复杂度 2）时间复杂度
'''

def n3(nums, n):
    '''
    :param nums: 数组
    :param n: 数组长度
    :return: 最大子列和
    '''
    max_sum = 0
    for i in range(n):
        for j in range(i, n+1):
            cur_sum = 0
            for k in range(i, j):
                cur_sum += nums[k]
            if cur_sum > max_sum:
                max_sum = cur_sum

    return max(0, max_sum)


def n2(nums, n):
    '''
    :param nums: 数组
    :param n: 数组长度
    :return: 最大子列和
    '''
    max_sum = 0
    for i in range(n):
        cur_sum = 0
        for j in range(i, n):
            cur_sum += nums[j]
            if cur_sum > max_sum:
                max_sum = cur_sum

    return max(0, max_sum)


def nlogn(nums, left, right):
    '''
    :param nums: 数组
    :param left: 左边界
    :param right: 右边界
    :return: 最大子列和
    '''

    if left == right: return nums[left]

    mid = (left+right) // 2

    left_maxSubseqSum = nlogn(nums, left, mid)
    right_maxSubseqSum = nlogn(nums, mid+1, right)

    max_leftBorderSum = 0
    tmp = 0
    for i in range(left, mid+1):
        tmp += nums[mid-i]
        if tmp>max_leftBorderSum:
            max_leftBorderSum = tmp

    max_rightBorderSum = 0
    tmp = 0
    for i in range(mid+1, right+1):
        tmp += nums[i]
        if tmp > max_rightBorderSum:
            max_rightBorderSum = tmp

    return max(left_maxSubseqSum, right_maxSubseqSum, max_leftBorderSum+max_rightBorderSum)


def n(nums, n):
    '''
    :param nums: 数组
    :param n: 数组长度
    :return: 最大子列和
    '''
    tmp = 0
    max_sum = 0
    for i in range(n):
        tmp += nums[i]
        if tmp > max_sum:
            max_sum = tmp
        elif tmp<0:
            tmp = 0

    return max_sum

if __name__ == '__main__':
    nums = [10, -10, 2, 5, -3, 8, 9, 6, 8, -13, 14, 5, -3, 6]
    print(n3(nums, len(nums)))
    print(n2(nums, len(nums)))
    print(nlogn(nums, 0, len(nums)-1))
    print(n(nums, len(nums)))
