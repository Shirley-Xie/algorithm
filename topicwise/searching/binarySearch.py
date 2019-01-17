 #coding:utf-8

# 1 分而治之，递归
def binarySearch_divCon(arr, l, r, x):
	# 这句不易想
	if r >= l:
	 	mid = l + (r-l)/2
	 	prv = arr[mid]
	 	if prv == x:return mid
	 	elif prv > x:
	 		return binarySearch_divCon(arr, l, mid-1, x)
	 	else:
	 		return binarySearch_divCon(arr, mid+1, r, x)
	else:
		return -1 		
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch_divCon(arr, 0, len(arr)-1, x)

if result != -1: 
    print("Element is present at index % d" % result )
else: 
    print("Element is not present in array")
