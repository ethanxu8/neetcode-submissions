class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i, num in enumerate(nums): 
            if target - num in hash: 
                return [hash[target-num], i]
            else: 
                hash[num] = i 


        # add all possble sums --> O(n^2) 
        # hashmap --> key:value pair num:ind 
            # targert - num in nums, and if target - num is in hashmap, return hashmap[key], ind
            # traverse through the array one time 
        