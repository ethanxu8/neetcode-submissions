class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r: 
            if nums[l] < nums[r]: 
                res = min (res, nums[l])
                break 
        
            m = (l + r) // 2
            res = min (res, nums[m])
            if nums[m] >= nums[l]: 
                l = m + 1
            else: 
                r = m - 1

        return res
        

        

# binary treee 

# base case: if the left node < right node then the
    # the minimum value would be the left node or the first number in the list 

# if left node < right node --> False it measn its not ascending 
    # check with a midpoint number 

# if left node < midpoint number then the min is in the second half 
# if left node > midpoint number then the min should be in the right half 
# do that until oyu find it 



        