#coding = 'utf-8'
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return []
        res = float('inf')
        nums.sort() #先进行排序O(nlgn)
        for i in range(n-2): #双层循环O(n^2)
            if i>0 and nums[i]==nums[i-1]:
                continue
            t = target-nums[i]
            l,e = i+1, n-1
            while l < e:
                temp = nums[l]+nums[e]
                if abs(temp+nums[i]-target) < abs(res-target):
                    res = temp+nums[i]
                if temp < t:
                    l += 1
                elif temp > t:
                    e -= 1
                else:
                    return res
        return res
