# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        last_node = ListNode(None)
        root_node = last_node
        add_one = 0
        while 1:
            if l1 is None and l2 is None:
                if add_one == 1:
                    last_node.next =  ListNode(1)
                break
            if l1 is None:
                l1_val = 0
            else:
                l1_val = l1.val
            if l2 is None:
                l2_val = 0
            else:
                l2_val = l2.val
            sum_value = l1_val + l2_val + add_one
            # print('%s = %s + %s + %s' % (sum_value, l1.val, l2.val, add_one))
            if sum_value >= 10:
                remain_value = sum_value - 10
                add_one = 1
            else:
                remain_value = sum_value
                add_one = 0
            now_node = ListNode(remain_value)
            last_node.next = now_node
            last_node = now_node
            # print(l1.val, l2.val, add_one)
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return root_node.next
        

def make_links(number_list):
    last_node = ListNode(None)
    root_node = last_node
    for num in number_list[::-1]:
        now_node = ListNode(num)
        last_node.next = now_node
        last_node = now_node
    return root_node.next


def get_number_from_links(number_links):
    num_list = []
    while number_links is not None:
        num_list.append(number_links.val)
        number_links = number_links.next
    return num_list


if __name__ == '__main__':
    # number1_list = [3,4,2]
    # number2_list = [4,6,5]    
    number1_list = [5]
    number2_list = [5]
    number1_links = make_links(number1_list)
    number2_links = make_links(number2_list)

    print(get_number_from_links(number1_links))
    print(get_number_from_links(number2_links))
    
    res = Solution().addTwoNumbers(number1_links, number2_links)
    print(get_number_from_links(res))






        