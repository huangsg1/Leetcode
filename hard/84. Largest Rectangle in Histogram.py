#coding=utf-8
class Solution(object):
    #方法一：一种改进的左右扫描法，利用已有的部分结果进行跳跃式的计算 
    #Time: O(n) Space:O(2*n)
    '''
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        n = len(heights)
        if n==1:
            return heights[0]
            
        #判断向后延伸的直方图个数
        right = [1 for i in range(n)]
        for i in range(n-2,-1,-1):
            j = i + 1
            while j < n and heights[i] <= heights[j]:
                j += right[j]
            right[i] = j - i
        
        #判断向前延伸的直方图个数
        left = [1 for i in range(n)]
        for i in range(1,n):
            j = i - 1
            while j >=0 and heights[i] <= heights[j]:
                j -= left[j]
            left[i] = i - j
    
        #遍历一次求最大的面积
        ans = 0
        for i in range(n):
            ans = max(ans, (left[i]+right[i]-1)*heights[i])
            
        return ans
    '''       
    #借助一个辅助的栈，每一个元素平均被访问两次
    #Time:O(n) Space:(n)
    def largestRectangleArea(self, heights):
        if not heights:
            return 0
        n = len(heights)
        if n == 1:
            return heights[0]
            
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
    
        
