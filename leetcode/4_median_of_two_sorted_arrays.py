def get_two_median_num_index_from_list(numslist):
    numslist_length = len(numslist)
    median = numslist_length / 2.0
    if numslist_length%2 == 1:
        # print('numslist_length%2:', numslist_length%2, 'median:', median)
        indexs_list = [int(median - 0.5)]
    else:
        indexs_list = [int(median - 1), int(median)]
    return indexs_list


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
    while len(items) < length:
        pop_num1 = nums1[nums1_start_pointer]
        pop_num2 = nums2[nums2_start_pointer]
        # print(pop_num1, pop_num2)
        if pop_num1 <= pop_num2:
            items.append(pop_num1)
            nums1_start_pointer += 1
        else:
            items.append(pop_num2)
            nums2_start_pointer += 1
    return items


def get_max_many_nums_from_two_numlist(nums1, nums2, length, nums1_start_pointer, nums2_start_pointer):
    items = []
    while len(items) < length:
        pop_num1 = nums1[nums1_start_pointer]
        pop_num2 = nums2[nums2_start_pointer]
        # print(pop_num1, pop_num2)
        if pop_num1 >= pop_num2:
            items.append(pop_num1)
            nums1_start_pointer -= 1
        else:
            items.append(pop_num2)
            nums2_start_pointer -= 1
    return items


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
        print('split min_nums:', left_list, middle_list, right_list)
        if len(middle_list) > 0:
            if len(indexs_list) > 1:
                middle_list.insert(0, median_list[0])
                middle_list.append(median_list[1])
            else:
                if median_list[0] >= middle_list[-1]:
                    middle_list.append(median_list[0])
                else:
                    middle_list.insert(0, median_list[0])
        else:
            middle_list = median_list

        differ_length = abs(len(left_list) - len(right_list))
        if len(left_list) < len(right_list):
            nums1_start_pointer = 0
            nums2_start_pointer = indexs_list[-1] + 1
            items = get_small_many_nums_from_two_numlist(right_list, max_nums, differ_length, nums1_start_pointer, nums2_start_pointer)
            middle_list = middle_list + items
        elif len(left_list) > len(right_list):
            nums1_start_pointer = len(left_list) - 1
            nums2_start_pointer = indexs_list[0] + 1
            items = get_max_many_nums_from_two_numlist(left_list, max_nums, differ_length, nums1_start_pointer, nums2_start_pointer)
            middle_list = items + middle_list
        else:
            items = []

        median_indexs = get_two_median_num_index_from_list(middle_list)
        median_list = [middle_list[index] for index in median_indexs]
        if len(median_list) == 1:
            return median_list[0]
        else:
            return sum(median_list) / 2.0


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


    numslist1 = [1,4,7,9,18,20, 39, 500]
    numslist2 = [5,11,17,25,190,210]
    print(numslist1)
    print(numslist2)
    res = Solution().findMedianSortedArrays(numslist1, numslist2)
    print(res)

    alllist = numslist1 + numslist2
    alllist.sort()
    indexs_list = get_two_median_num_index_from_list(alllist)
    print(alllist)
    for index in indexs_list:
        print(alllist[index])

    # nums1 = [1,4,7,9,18,20, 39, 450,498,500]
    # nums2 = [5,11,17,25,190,210]
    # length = 6
    # nums1_start_pointer = len(nums1) - 1
    # nums2_start_pointer = len(nums2) - 1
    # items = get_max_many_nums_from_two_numlist(nums1, nums2, length, nums1_start_pointer, nums2_start_pointer)
    # print(items)





