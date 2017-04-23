# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        if not root:
            return 0
        
        #left_d = self.help_fun(root.left)
        #right_d = self.help_fun(root.right)
        self.help_fun(root)
        return self.ans
        
    def help_fun(self,root):
        if not root:
            return 0
        else:
            left_d = self.help_fun(root.left)
            right_d = self.help_fun(root.right)
            d = max(left_d,right_d)
            self.ans = max(self.ans,left_d+right_d)
            return d+1
            
            
