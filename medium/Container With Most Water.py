class Solution:
    def maxArea(self, height):
        
        mostWater = 0
        start = 0
        finish = len(height) - 1

        while start < finish:
            gap = finish - start
            mostWater = max(gap * min(height[start], height[finish]), mostWater)

            if height[finish] < height[start]:
                finish -= 1
            elif height[finish] > height[start]:
                start += 1
            else:
                if height[start + 1] > height[finish - 1]:
                    start += 1
                elif height[start + 1] < height[finish - 1]:
                    finish -= 1
                else:
                    start += 1
        
        return mostWater