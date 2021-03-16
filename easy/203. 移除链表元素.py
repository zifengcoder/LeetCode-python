# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 判断一下空链表的情况
        if head == None:
            return None
        c = ListNode(0)
        prev =c
        while head:
            if head.val != val:
                prev.next = head
                prev = head
            head = head.next
            # 防止链表最后一位数值和val相等的情况
            if head == None:
                prev.next = None
        return c.next

    def removeElements2(self, head, val):
        sentinel = ListNode(0)
        sentinel.next = head

        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return sentinel.next

