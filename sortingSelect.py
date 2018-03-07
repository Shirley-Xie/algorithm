# 选择排序
# arr = [64, 34, 25, 12, 22, 11, 90]
arr = [4, 10, 13, 5, 1]
# 1：简单的选择
# 每次找到最小值将其排位,将索引记住不是值


def selectionSort(arr):
    n = len(arr)
    # k = 0
    for j in range(n):
        idx = j
        for i in range(j+1, n):
            if arr[idx] > arr[i]:
                idx = i
        arr[idx], arr[j] = arr[j], arr[idx]
    print(arr)

# selectionSort(arr)


# 2：堆排序
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1	 # left = 2*i + 1
    r = 2 * i + 2	 # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)
[4, 10, 13, 5, 1]

def heapSort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    print(arr)

heapSort(arr)
