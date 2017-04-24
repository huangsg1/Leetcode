#coding:'utf-8'
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 3:
            return []
        res = []
        nums.sort() #先进行排序O(nlgn)
        for i in range(n-2): #双层循环O(n^2)
            if i>0 and nums[i]==nums[i-1]:
                continue
            t = 0-nums[i]
            l,e = i+1, n-1
            while l < e:
                if nums[l]+nums[e] < t:
                    l += 1
                elif nums[l]+nums[e] > t:
                    e -= 1
                else:
                    if res and nums[l] == res[-1][1] and nums[e] == res[-1][2]:
                        l += 1
                        e -= 1
                    else:
                        res.append([nums[i],nums[l],nums[e]])
                        l += 1
                        e -= 1
        return res
