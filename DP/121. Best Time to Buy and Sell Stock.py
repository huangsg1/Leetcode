class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices)<2:
            return 0
            
        n = len(prices)
        cur_min = prices[0]
        res = 0
        for i in range(1,n):
            if prices[i] < cur_min:
                cur_min = prices[i]
            else:
                res = max(res, prices[i]-cur_min)
                
        return res
