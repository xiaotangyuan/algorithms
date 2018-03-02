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
        return left_max_nums[-1]
    if len(left_max_nums) == 0:
        return left_mini_nums[-1]
    return left_mini_nums[-1] if left_mini_nums[-1] > left_max_nums[-1] else left_max_nums[-1]


def get_mini_val_from_two_list(right_mini_nums, right_max_nums):
    if len(right_mini_nums) == 0:
        return right_max_nums[0]
    if len(right_mini_nums) == 0:
        return left_mini_nums[0]
    return right_mini_nums[0] if right_mini_nums[0] < right_max_nums[0] else right_max_nums[0]


class MeidanStack(object):
    def __init__(self):
        self.datas = []

    def add(self, num):
        if len(self.datas) == 0:
            self.datas.append(num)
            return None, None
        if len(self.datas) == 1:
            if num >= self.datas[0]:
                self.datas.append(num)
            else:
                self.datas.insert(0, num)
            return None, None
        else:
            if num <= self.datas[0]:
                self.datas.insert[0, num]
                right_popup = self.datas[-1]
                self.datas = self.datas[:2]
                return None, right_popup
            elif num >= self.datas[1]:
                self.datas.append(num)
                left_popup = self.datas[0]
                self.datas = self.datas[-2:]
                return left_popup, None



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
        print('max_nums:', left_max_nums, right_max_nums)

        left_mini_nums = []
        right_mini_nums = []

        def update_medians(num):
            left_max_val = get_max_val_from_two_list(left_mini_nums, left_max_nums)
            right_max_val = get_mini_val_from_two_list(right_mini_nums, right_max_nums)
            if num <= left_max_val:
                left_mini_nums.append(num)
                left_popup, right_popup = ms.add(left_max_val)
            elif num >= right_max_val:
                right_mini_nums.append(num)
                left_popup, right_popup = ms.add(right_max_val)
            else:
                left_popup, right_popup = ms.add(num)
            if left_popup:
                left_max_nums.append(left_popup)
            if right_popup:
                right_max_nums.insert(0, right_popup)



        for num in mini_nums:
            print('----------', left_mini_nums, left_max_nums, right_mini_nums, right_max_nums)
            if num <= left_max_nums[-1]:
                left_mini_nums.append(num)

            if num >= right_max_nums[0]:
                right_mini_nums.append(num)
            if len(medians) == 1:
                if num <= left_max_nums[-1]:
                    median_indexs.append(len(left_max_nums) - 1)



            if num > median1 and num < median2:
                left_mini_nums.append(median1)
                right_mini_nums.insert(0, median2)
                median2 = num
                median1 = num

            if num <= median1:
                left_mini_nums.append(num)
                median2 = median1
                median1 = get_max_val_from_two_list(left_mini_nums, left_max_nums)

            if num >= median2:
                right_mini_nums.append(num)
                median1 = median2
                median2 = get_mini_val_from_two_list(right_mini_nums, right_max_nums)
            print('num:', num, '  median:', median1, median2)
        return (median1 + median2) / 2




if __name__ == '__main__':
    # numslist = [1,2,3,4,5]
    # numslist = [1,2,3,4,6]
    # print(get_two_median_num_index_from_list(numslist))

    numslist1 = [1,4,7,9]
    numslist2 = [5,11,17,19,20]
    res = Solution().findMedianSortedArrays(numslist1, numslist2)
    print(res)
