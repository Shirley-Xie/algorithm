#coding:utf-8
# arr = [64, 34, 25, 12, 22, 11, 90]
arr = [4, 10, 13, 5, 1]
# 1：简单的选择
# 每次找到最小值将其排位,将索引记住不是值

# 简单查找，有序的，eg:电话簿中的名字是按字母顺序排列的

# 看电影找位子
'''
数组：内存中都是相连的，会额外占用空间，若多余申请位置则需整体转移,随机地读取元素时，数组的效率很高
读取O(1)：常量时间 *** （随机访问）
插入O(n)：线性时间
删除O(n)
'''

'''链表：可存储在内存的任何地方，当读取最后一个元素时需要跳跃效率低，若可以读取所有效率高。
读取O(n) （顺序访问）
插入O(1) ***
删除O(1) ***
链表数组
'''


'''
二分查找:找人名
O(logn)
'''

'''
快速排序
O(nlogn)
'''

'''
选择排序：按照歌曲播放次数最多的排序
O(n的平方)
''' 
A = [64, 25, 12, 22, 11] 

# Traverse through all array elements 
for i in range(len(A)-1, -1, -1): 
    # Find the minimum element in remaining 
    # unsorted array 
    max_idx = i 
    for j in range(0, i): 
        if A[max_idx] < A[j]: 
            max_idx = j     
    # Swap the found minimum element with 
    # the first element     
    A[i], A[max_idx] = A[max_idx], A[i] 
    # Driver code to test above 
print ("Sorted array", A) 


def selectionSort(arr):
    n = len(arr)
    # k = 0
    for i in range(n):
        min_idx = j
        for j in range(j+1, n):
            if arr[min_idx] > arr[i]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
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
