class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # edge case: 
        # if the number next is the same then continue 

        # sort nums 
        # have a left and right pointer and current value 
        # if three_sum > 0 then right pointer -= 1
        # if three_sum < 0 then left pointer += 1
        # else append indicies into a res list 
            # update the pointer by += l 
        
        res = []
        nums.sort()

        for i, v in enumerate(nums): 
            if i > 0 and v == nums[i - 1]: 
                continue 
            
            l, r = i + 1, len(nums) - 1
            while l < r: 
                three_sum = v + nums[l] + nums[r]
                if three_sum > 0: 
                    r -= 1 
                elif three_sum < 0: 
                    l += 1
                else: 
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]: 
                        l += 1
        
        return res


        
        # 0 - first element 
        # 