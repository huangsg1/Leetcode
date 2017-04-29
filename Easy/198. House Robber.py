#coding = utf-8
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        #空间优化
        s1,d1 = nums[0],0  
        # 状态转移
        for i in range(1,n):
            d = max(d1,s1)
            s = d1 + nums[i]
            d1,s1 = d,s
        return max(s1,d1)
