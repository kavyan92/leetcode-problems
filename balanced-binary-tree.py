"""Given a binary tree, determine if it is height-balanced. For this problem, a height-balanced binary tree is defined as: a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root)[0]

    def height(self, root):
        if not root:
            print(f'This an empty tree!')
            return True, 0
        print(f'Calling height for node {root.val}')
        is_left_balanced, left_height = self.height(root.left)
        is_right_balanced, right_height = self.height(root.right)
        
        is_balanced, current_height = \
            [is_left_balanced and is_right_balanced and (abs(left_height - right_height) <= 1), 1 + max(left_height, right_height)]
        
        return is_balanced, current_height
 
            