#coding = utf-8
#记忆化搜索
#对深度搜索进行优化，采用记忆
#time:O(m*n) space:O(m*n)
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        self.m,self.n = len(matrix),len(matrix[0])
        dp = [[-1 for i in range(self.n)] for j in range(self.m)]
        ans = 1
        
        self.dx,self.dy = [0,0,1,-1],[1,-1,0,0]
        for i in range(self.m):
            for j in range(self.n):
                ans = max(ans,self.dfs(i, j, matrix, dp))
        return ans
        
    def dfs(self, i, j, matrix, dp):
        if dp[i][j] != -1:
            return dp[i][j]
        ans = 1
        for x in range(4): 
            mx = i+self.dx[x]
            my = j+self.dy[x]
            if mx>=0 and mx<self.m and my>=0 and my<self.n:
                if matrix[mx][my] > matrix[i][j]:
                    ans = max(ans, self.dfs(mx,my,matrix,dp)+1)
        dp[i][j] = ans
        return ans
            
        
