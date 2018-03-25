# coding:utf-8

import copy

def sigmod(i, n):
    '''
    Σ 多项数求和 
    '''
    if not isinstance(i, int) or not isinstance(n, int):
        return False
    return reduce(lambda x, y: x+y, range(i, n+1))


def double_sigmod(a, b, i, j, func=None):
    '''
    双Σ求和
    '''
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(i, int) or not isinstance(j, int) or not func:
        return False

    result = 0
    for k in range(a, b+1):
        for n in range(i, j+1):
            result += func(n, k)

    return result


def continue_multiply(i, n):
    '''
    Π 连乘 
    '''
    if not isinstance(i, int) or not isinstance(n, int):
        return False
    return reduce(lambda x, y: x*y, range(i, n+1))


def factorial(n):
    '''
    n! 阶乘
    '''
    if not isinstance(n, int):
        return 'Invalid data, please input a int number'

    if n == 0 or n == 1:
        return 1

    else:
        return n * factorial(n-1)


def combination(iter=None, m=0):
    '''
    从 n 中选出 m 个，进行组合 
    '''
    result = []
    tmp = [0] * m
    length = len(iter)

    def next_num(li=0, ni=0):
        if ni == m:
            result.append(copy.copy(tmp))
            return
        for lj in range(li, length):
            tmp[ni] = iter[lj]
            next_num(lj + 1, ni + 1)

    next_num()
    return (result, len(result))


def permutation(iter=None, n=0):
    '''
     从 n 中选出 n 个，进行排列
    '''
    result = []
    tmp = [0] * n

    def next_num(arry, ni=0):
        if ni == n:
            result.append(copy.copy(tmp))
            return
        for lj in arry:
            tmp[ni] = lj
            arry_c = arry[:]
            arry_c.pop(arry.index(lj))
            next_num(arry_c, ni+1)

    next_num(iter[:], 0)
    return (result, len(result))


if __name__ == '__main__':
    # print double_sigmod(1, 2, 3, 4, lambda x, y: x+y)
    # print continue_multiply(5, 6)
    # print factorial(10)
    # print factorial(10)
    # print combination([1, 2, 3], 2)

    print permutation([1, 2, 3, 4, 5], 5)