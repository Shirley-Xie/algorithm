arr =   [12, 34, 54, 2, 3, 9, 10]
arr_s = [2, 3, 9, 10, 12, 34, 54]
n = len(arr_s)
x = 54
# 判断找不到的情况和找的到的情况


# 1 线性查找，就是一个个找
def linearSearch(arr, x):
    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return i
    return -1
# linearSearch(arr, 3)


# l+1取代for循环
def linearSearch_rec(arr, l, r, x):
    if r < l:
        return -1
    if arr[l] == x:
        return l
    return linearSearch_rec(arr, l+1, r, x)

# linearSearch_rec(arr, 0, n - 1, x)


# 2 二分查找, 有序的
def binarySearch1(arr, x, low, high):
    # 使用循环操作
    first = low
    last = high - 1
    found = False
    # 可以不用等于号？
    while first <= last and not found:
        mid = (first + last) // 2
        if arr[mid] == x:
            # return True
            found = True
        elif x < arr[mid]:
                last = mid - 1
        else:
            first = mid + 1
    return found

a = binarySearch1(arr_s, x, 0, n)
print(a)


def binarySearch2(arr, x, low, high):
    # 将值和zhong的比较，进行范围锁定
    # 这里的high 和low 不可以更改赋值
    if high >= low:
        mid = low + (high - low) // 2
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
        return binarySearch2(arr, x, low, high)
    else:
        return -1
re = binarySearch2(arr_s, x, 0, n)
print('binarySearch2:', re)

# 3 跳跃搜索, 确定范围再逐步查找
# Python3 code to implement Jump Search
import math


def jumpSearch(arr, x, n):
    step = math.sqrt(n)
    prev = 0
    while arr[int(min(step, n) - 1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    while arr[int(prev)] < x:
        prev += 1

        if prev == min(step, n):
            return -1

    if arr[int(prev)] == x:
        return prev

    return -1
jump = jumpSearch(arr_s, x, n)
print(jump)


# 4 插值搜索
def interpolationSearch(arr, n, x):
    # Find indexs of two corners
    lo = 0
    hi = (n - 1)

    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        # Probing the position with keeping
        # uniform distribution in mind.
        pos = lo + int(((float(hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo])))

        # Condition of target found
        if arr[pos] == x:
            return pos

        # If x is larger, x is in upper part
        if arr[pos] < x:
            lo = pos + 1

        # If x is smaller, x is in lower part
        else:
            hi = pos - 1

    return -1
out = interpolationSearch(arr_s, n, x)
print('interpolationSearch', out)


# 5 指数搜索
def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2

        # If the element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If the element is smaller than mid, then it
        # can only be present in the left subarray
        if arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        # Else he element can only be present in the right
        return binarySearch(arr, mid + 1, r, x)

    # We reach here if the element is not present
    return -1
# Returns the position of first
# occurence of x in array
def exponentialSearch(arr, n, x):
    # IF x is present at first location itself
    if arr[0] == x:
        return 0

    # Find range for binary seaarchj by repeated doubling
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2

    # Call binary search for the found range
    return binarySearch(arr, i//2, min(i, n), x)

expon = exponentialSearch(arr_s, n, x)
print(expon)