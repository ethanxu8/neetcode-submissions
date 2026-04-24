class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # brute force would be to find the min then add 1 
        # have a counter thats most so max consecutives 
        # then have one thats curr 
        # then do max(curr, most)

        # sort the list so that its in ascending order 
        # then find the number of consecutives 

        if not nums: 
            return 0 

        sorted_nums = sorted(nums)
        
        most = 1 
        curr = 1 

        for i in range(1, len(sorted_nums)): 
            if sorted_nums[i] == sorted_nums[i-1] + 1: 
                curr += 1
            elif sorted_nums[i] != sorted_nums[i-1]: 
                curr = 1
            most = max(most, curr) 

        return most 




