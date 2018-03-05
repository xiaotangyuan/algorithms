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


def gen_new_median_list(median_list, num):
    if len(median_list) == 0:
        median_list.append(num)
        return median_list, None, None
    if len(median_list) == 1:
        if num >= median_list[0]:
            median_list.append(num)
        else:
            median_list.insert(0, num)
        return median_list, None, None
    else:
        if num <= median_list[0]:
            median_list.insert(0, num)
            right_popup = median_list[-1]
            median_list = median_list[:2]
            return median_list, None, right_popup
        elif num >= median_list[1]:
            median_list.append(num)
            left_popup = median_list[0]
            median_list = median_list[-2:]
            return median_list, left_popup, None
        else:
            left_popup, right_popup = median_list[0], median_list[1]
            median_list = [num]
            return median_list, left_popup, right_popup


def split_numlist_to_three_list_by_medianlist(numlist, median_list):
    left_list = []
    middle_list = []
    right_list = []

    for num in numlist:
        if num <= median_list[0]:
            left_list.append(num)
        elif num >= median_list[-1]:
            right_list.append(num)
        else:
            middle_list.append(num)
    return left_list, middle_list, right_list


def get_small_many_nums_from_two_numlist(nums1, nums2, length, nums1_start_pointer, nums2_start_pointer):
    items = []
    while len(items) <= length:
        pop_num1 = nums1[nums1_start_pointer]
        pop_num2 = nums2[nums2_start_pointer]
        if pop_num1 <= pop_num2:
            if len(items) < length:
                items.append(pop_num1)
                nums1_start_pointer += 1
            if len(items) < length:
                items.append(pop_num2)
                nums1_start_pointer += 1


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

        median_list = []
        for index in indexs_list:
            median_list, left_popup, right_popup = gen_new_median_list(median_list, max_nums[index])

        print('init median_list:', median_list, 'index of', indexs_list)

        left_list = []
        middle_list = []
        right_list = []

        for num in min_nums:
            if num <= median_list[0]:
                left_list.append(num)
            elif num >= median_list[-1]:
                right_list.append(num)
            else:
                middle_list.append(num)

        differ_length = abs(len(left_list) - len(right_list))
        if len(left_list) > len(right_list):
            while differ_length:
                differ_length -= 1



        elif len(left_list) < len(right_list):
            



        print('split min_nums:', left_list, middle_list, right_list)


        print(median_list)
        print(sum(median_list)/2.0)


if __name__ == '__main__':

    # median_list = [1,5]
    # num = 1
    # median_list, left_popup, right_popup = gen_new_median_list(median_list, num)
    # print(median_list, left_popup, right_popup)

    # numlist = [1, 4, 7, 9, 18, 29, 39, 500]
    # medianlist = [19,21]
    # print(split_numlist_to_three_list_by_medianlist(numlist, medianlist))

    # numslist = [1,2,3,4,5]
    # numslist = [1,2,3,4,6]
    # print(get_two_median_num_index_from_list(numslist))

    # ms = MeidanStack()
    # for item in [2, 10,9,4,6,1]:
    #   ms.add(item)
    #   print(ms)

    numslist1 = [1,4,7,9,18,20, 39, 500]
    numslist2 = [5,11,17,25,190,210]
    print(numslist1)
    print(numslist2)
    res = Solution().findMedianSortedArrays(numslist1, numslist2)
    print(res)


