"""Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one."""

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        
        current = head
        
        while current:
            nodes.append(current)
            current = current.next
            
        middle = int((len(nodes)/2))
        
        return nodes[middle]

"""Runtime: 32 ms, faster than 67.01% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 14.2 MB, less than 74.13% of Python3 online submissions for Middle of the Linked List."""