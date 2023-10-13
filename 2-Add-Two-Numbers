
#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807. 
#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        num2 = ''
        node1 = l1
        node2 = l2

        while node1 is not None:
            num1 = str(node1.val) + num1
            node1 = node1.next
        while node2 is not None:
            num2 = str(node2.val) + num2
            node2 = node2.next
        num1 = int(num1)
        num2 = int(num2)
        num_sum = num1 + num2
        str_sum = str(num_sum)
        
        num_nodes = list(str_sum)
        
        for indx, num in enumerate(str_sum):
            if indx == 0:
                num_nodes[indx] = ListNode(val = num, next=None)
            else: 
                num_nodes[indx] = ListNode(val = num, next=num_nodes[indx-1])
            
        result = num_nodes[len(num_nodes)-1]
        return result
            
        


        

            





