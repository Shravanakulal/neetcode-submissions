# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        arr2 = []

        curr = list1
        while curr:
            arr1.append(curr.val)
            curr = curr.next

        curr = list2
        while curr:
            arr2.append(curr.val)
            curr = curr.next

        i = 0
        j = 0
        arr = []

        while i<len(arr1) and j<len(arr2):
            if arr1[i] <= arr2[j]:
                arr.append(arr1[i])
                i += 1
            else:
                arr.append(arr2[j])
                j += 1

        while i < len(arr1):
            arr.append(arr1[i])
            i += 1

        while j < len(arr2):
            arr.append(arr2[j])
            j += 1

        dummy = ListNode(0)
        curr = dummy

        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next

        