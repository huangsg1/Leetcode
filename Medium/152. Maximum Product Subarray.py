#coding=utf-8
#局部最优与全局最优，通过局部最优获得全局最优
#局部最优指的是以当前元素作为结尾能取得的最值，全局的话不一定以当前元素作为结尾
#Time:O(n) Space:O(n)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==1:
            return nums[0]
        #状态方程
        dpmin = [float('inf') for i in range(n)]
        dpmax = [float('-inf') for i in range(n)]
        dpmin[0] = dpmax[0] = nums[0]
        
        #状态转移
        res = nums[0]
        for i in range(1,n):
            dpmin[i] = min(nums[i],min(dpmax[i-1]*nums[i],dpmin[i-1]*nums[i]))
            dpmax[i] = max(nums[i],max(dpmax[i-1]*nums[i],dpmin[i-1]*nums[i]))
            res = max(res,dpmax[i]) #全局考虑
        
        return res
