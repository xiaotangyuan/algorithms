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
            max_nums = nums1
            mini_nums = nums2
        else:
            max_nums = nums2
            mini_nums = nums1
        median_indexs = get_two_median_num_index_from_list(max_nums)
        print('median_indexs:', median_indexs)

        if len(median_indexs) == 1:
            median_index_left, median_index_right  = median_indexs[0], median_indexs[0]
            medians = [max_nums[median_indexs[0]]]
        else:
            median_index_left, median_index_right  = median_indexs[0], median_indexs[1]
            medians = [max_nums[median_indexs[0]], max_nums[median_indexs[1]]]
        ms = MeidanStack()
        ms.datas = medians

        left_max_nums = max_nums[:median_index_left]
        right_max_nums = max_nums[median_index_right+1:]
        print(ms)

        left_mini_nums = []
        right_mini_nums = []

        def update_medians(num):
            print(get_max_val_from_two_list(left_mini_nums, left_max_nums))
            left_max_val, the_target_left_list = get_max_val_from_two_list(left_mini_nums, left_max_nums)
            right_max_val, the_target_right_val = get_mini_val_from_two_list(right_mini_nums, right_max_nums)
            if num <= left_max_val:
                left_mini_nums.append(num)
                left_popup, right_popup = ms.add(left_max_val)
                the_target_left_list.pop()
            elif num >= right_max_val:
                right_mini_nums.append(num)
                left_popup, right_popup = ms.add(right_max_val)
                the_target_right_list.pop(0)
            else:
                left_popup, right_popup = ms.add(num)
            if left_popup:
                left_max_nums.append(left_popup)
            if right_popup:
                right_max_nums.insert(0, right_popup)
            print('--%s--:' % num, left_max_val, right_max_val, left_popup, right_popup)

        for num in mini_nums:
            print('----------', left_mini_nums, left_max_nums, right_mini_nums, right_max_nums)
            update_medians(num)
            print(ms)

        median1, median2 = ms.datas[0], ms.datas[1]
        return (median1 + median2) / 2


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






