# coding=utf-8
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head) :
        # 方法1：递推
        pre = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

        # 方法2：递归

        # def reverse_lined_list(node, pre):
        #     if not node:
        #         return pre
        #
        #     temp_node = node.next
        #     node.next = pre
        #
        #     return reverse_lined_list(temp_node, node)
        #
        # return reverse_lined_list(head, None)


if __name__ == '__main__':
    obj = Solution()
    head = ListNode([1, 2, 3, 4, 5])
    print obj.reverseList(head=head).val