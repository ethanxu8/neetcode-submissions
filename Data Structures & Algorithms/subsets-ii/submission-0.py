class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort() 

        def backtrack(start, path): 
            
            result.append(path[:])

            for i in range(start, len(nums)): 
                if i > start and nums[i] == nums[i-1]: 
                    continue 
                
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        
        backtrack(0, [])
        return result


# base case: 
    # if index = len(nums): 
        # result.append(path[:])
        # return 
    

    # for i in range(start, len(nums)): 
        # if i > start and nums[i] == nums[i-1]: 
            # continue 
        
    
    # path.append(nums[i])
    # backtrack(index+1, path)
    # path.pop()

# back
        