# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def get_step_and_sig_val(l1, l2, step):
    if l1 is None:
        int1 = 0
    else:
        int1 = l1.val
    if l2 is None:
        int2 = 0
    else:
        int2 = l2.val
    sum_val = int1 + int2 + step
    if sum_val >= 10:
        step = 1
        sig_val = sum_val - 10
    else:
        step = 0
        sig_val = sum_val
    return step, sig_val


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        last_node = ListNode(None)
        root_node = last_node
        step = 0
        while 1:
            if l1 is None and l2 is None:
                break
            step, sig_val = get_step_and_sig_val(l1, l2, step)
            now_node = ListNode(sig_val)
            last_node.next = now_node
            last_node = now_node
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
    number1_list = [3,4,2]
    number2_list = [4,6,5]    
    # number1_list = [5]
    # number2_list = [5]
    number1_links = make_links(number1_list)
    number2_links = make_links(number2_list)

    print(get_number_from_links(number1_links))
    print(get_number_from_links(number2_links))
    
    res = Solution().addTwoNumbers(number1_links, number2_links)
    print(get_number_from_links(res))






        