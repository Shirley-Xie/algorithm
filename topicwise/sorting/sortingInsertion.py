arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# 插入排序
# 1：直接插入,
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp
    print('insertionSort:', arr)
insertionSort(arr)


# 2：折半插入
def binary_search(arr, val, start, end):

    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1
    elif start > end:
        return start
    else:
        mid = (start + end) // 2
        if val == arr[mid]:
            return mid
        elif val > arr[mid]:
            binary_search(arr, val, mid+1, end)
        else:
            binary_search(arr, val, start, mid-1)


def insertion_sort(arr):
    # 循环从第二个开始，找其前面恰当位置插入
    n = len(arr)
    for i in range(1, n):
        val = arr[i]
        j = binary_search(arr, val, 0, n-1)
        arr = arr[:j] + val + arr[j:i] + arr[i+1:]

print(insertion_sort([27, 31, 4, 12, 3, 5, 4, 5]))


# 3：希尔排序, 交换条件，启始位置，截止判断条件
def shellSort(arr):
    n = len(arr)
    gap = n // 2
    # 间隔之前比较， 截止位置,
    while gap > 0:
        for i in range(gap, n):
            # 将第一个作为比较对象
            temp = arr[i]
            j = i
            # 从gap的第一个位置开始
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2
# Driver code to test above
shellSort(arr)
print('shellsort:', arr)

# 归并排序
