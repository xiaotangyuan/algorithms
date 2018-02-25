"""
二分查找算法
"""

data = [1,3,5,4,6,8,9,89,100]


def binary_search(data, num):
	start_index = 0
	end_index = len(data) - 1
	loop = True
	loop_num = 0
	while loop:
		loop_num += 1
		if loop_num > 10:
			return
		check_index = (end_index-start_index)//2 + start_index
		tar_value = data[check_index]
		print('check_index:', check_index, ' tar_value:', tar_value)
		if num > tar_value:
			print('%s > %s' % (num, tar_value))
			start_index = check_index
		elif num < tar_value:
			print('%s < %s' % (num, tar_value))
			end_index = check_index
		else:
			return num, check_index
	return num, 'not in data'


if __name__ == '__main__':
	import sys
	num = sys.argv[1]
	print(binary_search(data, int(num)))
