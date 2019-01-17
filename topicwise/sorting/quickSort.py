#coding:utf-8

# 并未搞清楚
def partition(arr, low, high):
	i = (low - 1) 
	pivot = arr[high] 

   	for j in range(low , high): 
		if arr[j] <= pivot:
	    	i = i + 1
	        arr[i], arr[j] = arr[j], arr[i]

	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return (i + 1)

# 快速
def quickSort_recur(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort_recur(arr, low, pi - 1)
        quickSort_recur(arr, pi + 1, high)

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort_recur(arr, 0, n - 1)  
print(arr)     