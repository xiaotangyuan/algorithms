class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_cache_list = []
        cur_cache_list = []
        for i in s:
            if i not in cur_cache_list:
                in_index = -1
            else:
                in_index = cur_cache_list.index(i)
            if in_index > -1:
                if len(cur_cache_list) > len(max_cache_list):
                    max_cache_list = cur_cache_list.copy()
                cur_cache_list = cur_cache_list[in_index+1:]
                print('in in_index:', cur_cache_list)
            cur_cache_list.append(i)
            print(cur_cache_list, max_cache_list)
        if len(cur_cache_list) > len(max_cache_list):
            max_cache_list = cur_cache_list.copy()
        return len(max_cache_list)

 

if __name__ == '__main__':
    s = 'cbdd'
    s = 'cb'
    s = 'dvdf'
    s = 'abcdeeee123485948'
    s = 'abcabcbb'
    print(Solution().lengthOfLongestSubstring(s))
