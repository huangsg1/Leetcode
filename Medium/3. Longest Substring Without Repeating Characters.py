#coding:utf-8
#time:(n^2)
#space:(2*n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n<=1:
            return n
        d = {}
        res = 0
        l = 0
        temp = 0
        for i in range(n):
            if s[i] not in d:
                d[s[i]] = i
                temp += 1
            else:
                if d[s[i]] >= l:
                    res = max(res, temp)
                    temp = temp - (d[s[i]]-l)
                    l = d[s[i]]+1
                else:
                    temp += 1
                d[s[i]] = i
    
        return max(res,temp)
                
        
