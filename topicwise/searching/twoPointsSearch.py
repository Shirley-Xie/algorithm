#coding:utf-8
arr =   [12, 34, 54, 2, 3, 9, 10]
arr_s = [2, 3, 9, 10, 12, 34, 54]
n = len(arr)
x = 54


"""
如果使用循环，程序的性能可能更高;如果使用递归，程序可能
 更容易理解。如何选择要看什么对你来说更重要

 基线条件：函数不用调用自己，避免成死循环
 递归条件：函数调用自己

 栈：压入（插入）和弹出（删除并读取）=> 取盘子
"""

# 求和数组，使用循环
def sum(arr): 
	total = 0
	for x in arr:
	total += x return total

print(sum([1, 2, 3, 4]))

'''
使用递归
1 基线条件：最简单的数组？数组为空或者只包含一个元素
2 递归条件：缩小规模？归纳
'''
def sum(x):
	total = 0 
	return sum(x += x )


# 1:只包含一个元素或为空
def quicksort(array): 
	if len(array) < 2:
		return array
"""
2:对于更长的数组：
  基准值 priot:数组的第一个元素
  分区：比基准值大的字数组，比基准值小的子数组，基准值。即左边的数组 + 基准值 + 右边的数组

"""
quicksort([15, 10]) + [33] + quicksort([])


