#coding='utf-8'
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m,n = len(matrix),len(matrix[0])
        res = 0
        #状态定义及初始化
        dp = [[0 for i in range(n)] for j in range(min(2,m))]
        
        for i in range(min(2,m)):
            dp[i][0] = int(matrix[i][0])
            if dp[i][0] == 1:
                res = 1
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            if dp[0][j] == 1:
                res = 1
        #状态转移方程
        for i in range(1,m):
            for j in range(n):
                if j == 0:
                    dp[i&1][j] = int(matrix[i][j])
                elif matrix[i][j] == '1':
                    dp[i&1][j] = min(dp[(i-1)&1][j-1], min(dp[(i-1)&1][j],dp[i&1][j-1])) + 1
                else:
                    dp[i&1][j] = 0
                res = max(res, dp[i&1][j])    
        
        #输出结果
        return res*res
