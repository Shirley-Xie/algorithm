# 交换排序
arr = [64, 34, 25, 12, 22, 11, 90]


# 1：冒泡,重点是每次减少一个排序个数
def bubbleSort(arr):
    n = len(arr)
    # 循环次数
    for i in range(n):
        for j in range(1, n-i):
            # 判断交换
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    print(arr)
# bubbleSort(arr)


# 冒泡迭代
def bubbleSort_recursive(arr):
    # 内层自己调用自己处理
    for i, num in enumerate(arr):
            # 判断交换
            try:
                if num > arr[i+1]:
                    arr[i] = arr[i+1]
                    arr[i+1] = num
                    bubbleSort_recursive(arr)
            except IndexError:
                pass
    return arr
# bubbleSort_recursive(arr)


# 2：快速
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def quickSort_recursive(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
