# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)

        while list1:
            self.insert(dummy, list1.val)
            list1 = list1.next

        while list2:
            self.insert(dummy, list2.val)
            list2 = list2.next

        return dummy.next

    def insert(self, dummy, value):
        curr = dummy

        while curr.next and curr.next.val < value:
            curr = curr.next

        new_node = ListNode(value)
        new_node.next = curr.next
        curr.next = new_node