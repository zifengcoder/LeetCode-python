# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a, b = l1, l2
        # 伪头节点
        c = ListNode(0)
        prev = c
        while a and b:
            if a.val<=b.val:
                prev.next = a
                a = a.next
            else:
                prev.next = b
                b = b.next
            prev = prev.next
        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = a if a is not None else b
        return c.next