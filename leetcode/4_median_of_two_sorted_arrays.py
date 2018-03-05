def get_two_median_num_index_from_list(numslist):
    numslist_length = len(numslist)
    median = numslist_length / 2.0
    if numslist_length%2 == 1:
        # print('numslist_length%2:', numslist_length%2, 'median:', median)
        indexs_list = [int(median - 0.5)]
    else:
        indexs_list = [int(median - 1), int(median)]
    return indexs_list


def get_max_val_from_two_list(left_mini_nums, left_max_nums):
    if len(left_mini_nums) == 0:
        return left_max_nums[-1], left_max_nums
    if len(left_max_nums) == 0:
        return left_mini_nums[-1], left_mini_nums
    return left_mini_nums[-1], left_mini_nums if left_mini_nums[-1] > left_max_nums[-1] else left_max_nums[-1], left_max_nums


def get_mini_val_from_two_list(right_mini_nums, right_max_nums):
    if len(right_mini_nums) == 0:
        return right_max_nums[0], right_max_nums
    if len(right_mini_nums) == 0:
        return left_mini_nums[0], left_mini_nums
    return right_mini_nums[0], right_mini_nums if right_mini_nums[0] < right_max_nums[0] else right_max_nums[0], right_max_nums


class MedianItem(object):
	def __init__(self, num_index, num_list):
		self.num_index = num_index
		self.num_list = num_list

	def get_val(self):
		return self.num_list[self.num_index]


class MeidanStack(object):
    def __init__(self):
        self.items = []

    def add(self, medianitem):
    	medianitem_val = medianitem.get_val()
        if len(self.items) == 0:
            self.items.append(medianitem)
            return None, None
        if len(self.items) == 1:
            if medianitem_val >= self.items[0]:
                self.items.append(medianitem)
            else:
                self.items.insert(0, medianitem)
            return None, None
        else:
            if medianitem_val <= self.items[0]:
                self.items.insert(0, medianitem)
                right_popup = self.items[-1]
                self.items = self.items[:2]
                return None, right_popup
            elif medianitem_val >= self.items[1]:
                self.items.append(medianitem)
                left_popup = self.items[0]
                self.items = self.items[-2:]
                return left_popup, None
            else:
            	left_popup, right_popup = self.items[0], self.items[1]
            	self.items = [medianitem]
            	return left_popup, right_popup

    def __str__(self):
    	if len(self.items) == 2:
    		s = '%s , %s' % (self.items[0], self.items[1])
    	elif len(self.items) == 1:
    		s = '%s' % self.items[0]
    	else:
    		s = ''
    	return s


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
        	max_nums, min_nums = nums1, nums2
        else:
        	max_nums, min_nums = nums2, nums1
        indexs_list = get_two_median_num_index_from_list(max_nums)

        left_of_min_nums = []
        middle_of_min_nums = []
        right_of_min_nums = []

        for num in min_nums:
        	if num <= indexs_list[0]:
        		left_of_min_nums.append(num)
        	elif num >= indexs_list[-1]:
        		right_of_min_nums.append(num)
        	else:
        		middle_of_min_nums.append(num)

        left_pointer_index_of_max_nums = indexs_list[0] - 1
        right_pointer_index_of_max_nums = indexs_list[-1] + 1

        left_of_min_nums_pointer_index = len(left_of_min_nums) - 1
        right_of_min_nums_pointer_index = 0

        def get_all_left_nums_length(left_pointer_index_of_max_nums, left_of_min_nums_pointer_index):
        	left_of_max_nums_length = left_pointer_index_of_max_nums + 1
        	left_of_min_nums_length = len(left_of_min_nums) - left_of_min_nums_pointer_index - 1
        	return left_of_max_nums_length + left_of_min_nums_length

        def get_all_right_nums_length(right_pointer_index_of_max_nums, right_of_min_nums_pointer_index):
        	right_of_max_nums = len(max_nums) - right_pointer_index_of_max_nums - 1
        	right_of_min_nums =  len(right_of_min_nums) - right_of_min_nums_pointer_index - 1
        	return right_of_max_nums + right_of_min_nums

       	left_length = get_all_left_nums_length(left_pointer_index_of_max_nums, left_of_min_nums_pointer_index)
       	right_length = get_all_right_nums_length(right_pointer_index_of_max_nums, right_of_min_nums_pointer_index)
        

        while left_length != right_length:
        	if left_length > right_length:
        		# find max num , and its index
        		if max_nums[left_pointer_index_of_max_nums] >= left_of_min_nums[left_of_min_nums_pointer_index]:
        			left_pointer_index_of_max_nums -= 1
        		else:
        			left_of_min_nums_pointer_index -= 1
        	else:
      			if max_nums[right_pointer_index_of_max_nums] <= right_of_min_nums[right_of_min_nums_pointer_index]:
      				right_pointer_index_of_max_nums += 1
      			else:
      				right_of_min_nums_pointer_index += 1
      		left_length = get_all_left_nums_length(left_pointer_index_of_max_nums, left_of_min_nums_pointer_index)
       		right_length = get_all_right_nums_length(right_pointer_index_of_max_nums, right_of_min_nums_pointer_index)

 


if __name__ == '__main__':
    # numslist = [1,2,3,4,5]
    # numslist = [1,2,3,4,6]
    # print(get_two_median_num_index_from_list(numslist))

    # ms = MeidanStack()
    # for item in [2, 10,9,4,6,1]:
    # 	ms.add(item)
    # 	print(ms)

    numslist1 = [1,4,7,9]
    numslist2 = [5,11,17,19,20]
    print(numslist1)
    print(numslist2)
    res = Solution().findMedianSortedArrays(numslist1, numslist2)
    print(res)






