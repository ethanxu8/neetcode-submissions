class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev = []

        for num in nums: 
            if num in prev: 
                return True 
            else: 
                prev.append(num)
            
        return False

        # prev --> list of previous numbers and if num in nums in prev return false
        