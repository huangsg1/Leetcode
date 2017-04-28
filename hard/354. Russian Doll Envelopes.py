#coding=utf-8
class Solution(object):
    def help_cmp(self, a1, a2): #比较函数，第二个元素逆序
        if a1[0] == a2[0]:
            return a2[1] - a1[1]
        else:
            return a1[0] - a2[0]
    def help_search(self, arr, k): #二分法
        s, e = 0, len(arr)-1
        while s <= e:
            mid = (s+e)/2
            if arr[mid][1] >= k[1]:
                e = mid -1
            else:
                s = mid +1
        return e
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        if n <= 1:
            return n
        arr = sorted(envelopes, cmp=self.help_cmp)
        dp = [[0,0],arr[0]]
        for i in range(1, n):
            e = self.help_search(dp,arr[i])
            if e==0:
                dp[1] = arr[i]
            elif e==len(dp)-1:
                dp.append(arr[i])
            else:
                dp[e+1] = arr[i]
        return len(dp)-1
