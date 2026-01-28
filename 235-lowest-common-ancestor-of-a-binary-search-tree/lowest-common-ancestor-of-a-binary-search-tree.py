# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root
        while current:
            #case 1: both nodes are smaller than current --> go left
            if p.val < current.val and q.val < current.val:
                current = current.left
            #case 2: both nodes are greater than current --> go right
            elif p.val > current.val and q.val > current.val:
                current = current.right
            #case 3: nodes are on different sides 
            else:
                return current
        
        