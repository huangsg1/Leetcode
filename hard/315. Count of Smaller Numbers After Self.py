#coding:utf-8
#该题可以转化为逆序对的问题
class Node(object):
    def __init__(self,val):
        self.val = val
        self.num = 0
        self.left = None
        self.right = None
        
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        n = len(nums)
        res = [0 for i in range(n)]
        root = Node(nums[-1])
        for i in range(n-2,-1,-1):
            cur = root
            temp = 0
            while cur:
                pre = cur
                if nums[i] > cur.val:
                    temp += (cur.num + 1)
                    cur = cur.right
                    if not cur:
                        pre.right = Node(nums[i])
                else:
                    cur.num += 1
                    cur = cur.left
                    if not cur:
                        pre.left = Node(nums[i])
            else:
                res[i] = temp
        return res
            
                    
