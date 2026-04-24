class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights) - 1
        max_area = (r - l) * min(heights[l], heights[r])

        while l < r: 
            if heights[l] <= heights[r]:
                l += 1 # left is less than right abandon left
            else: 
                r -= 1
            max_area = max(max_area, (r - l) * min(heights[l], heights[r]))
        
        return max_area
            
        # area = (index diff) * min(two numbers)
        # have two pointers that start at the ends and then eliminate the lesser one 
        
        # initalize a max_area and then replace with max(max_area, current_area)
        