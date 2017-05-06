#coding=utf-8
#Time: O(n^2) Space:O(n)
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m,n = len(matrix),len(matrix[0])
        heights = map(int, matrix[0])
        ans = self.help(heights)
        for i in range(1,m):
            for j in range(n):
                if matrix[i][j]=='0':
                    heights[j] = 0
                else:
                    heights[j] += 1
            ans = max(ans, self.help(heights))
        return ans
            
    def help(self, heights):
        n = len(heights)
        ans = 0
        my_stack = []
        heights.append(0)
        for i in range(n+1):
            if not my_stack or heights[i]>=heights[my_stack[-1]]:
                my_stack.append(i)
            else:
                while my_stack and heights[my_stack[-1]]>heights[i]:
                    top_index = my_stack[-1]
                    my_stack.pop()
                    if not my_stack:
                        w = i
                    else:
                        w = i - my_stack[-1] - 1
                    ans = max(ans, heights[top_index]*w)
                my_stack.append(i)
        return ans
