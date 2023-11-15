class Solution:
    def largestRectangleArea(self, heights) -> int:
        
        stack = []
        rectMax = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                rectMax = max(rectMax, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return rectMax
