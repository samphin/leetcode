# encoding='utf-8'

'''
   author:zhangyu
   date:2019.8.4
   description:找到两个数组中的交集
'''


def get_intersection(arr1, arr2):
    '''
        两个数组求交集
    Args:
        arr1: 数组1
        arr2: 数组2

    Returns:
        数组交集
    '''
    arr1.sort();
    arr2.sort();
    arr = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            arr.append(arr1[i])
            i += 1
            j += 1
    return arr


def get_intersection2(arr1, arr2):
    '''
        两个数组求交集
    Args:
        arr1: 数组1
        arr2: 数组2

    Returns:
        数组交集
    '''
    arr = []
    s1 = set()
    for ele in arr1:
        s1.add(ele)
    s2 = set()
    for ele in arr2:
        s2.add(ele)
    for ele in s1:
        if s2.__contains__(ele):
            arr.append(ele)
    return arr


def get_intersection3(arr1, arr2):
    '''
        两个数组求交集
    Args:
        arr1: 数组1
        arr2: 数组2

    Returns:
        数组交集
    '''
    s = set()
    for ele in arr1:
        s.add(ele)
    arr = []
    for ele in arr2:
        if s.__contains__(ele):
            arr.append(ele)
            s.remove(ele)
    return arr


if __name__ == '__main__':
    arr1 = [1, 2, 3, 1]
    arr2 = [2, 3, 4, 2]
    arr = get_intersection(arr1, arr2)
    print(arr)
