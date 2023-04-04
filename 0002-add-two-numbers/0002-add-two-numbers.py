# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ans = (l1.val + l2.val) % 10
        carry = int((l1.val + l2.val) / 10)
        solution = ListNode(ans, None)

        # when the next node of l2 and l1 are none
        if l2.next == None and l1.next == None:
            if carry == 0:
                solution.next = None
            else:
                solution.next = ListNode(carry, None)
            return solution

        # when the next node of l1 is none
        if l1.next == None and l2.next != None:
            carryNode = ListNode(carry, None)
            solution.next = Solution().addTwoNumbers(carryNode, l2.next)
            return solution

        # when the next node of l2 is none
        if l2.next == None and l1.next != None:
            carryNode = ListNode(carry, None)
            solution.next = Solution().addTwoNumbers(carryNode, l1.next)
            return solution

        # when the next node of l2 and l1 are not none
        next_val = l1.next.val + carry
        nextNode = ListNode(next_val, l1.next.next)
        solution.next = Solution().addTwoNumbers(nextNode, l2.next)
        return solution