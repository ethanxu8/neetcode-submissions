class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        used = [False] * len(nums)

        def backtrack(path): 

            # base case
            if len(path) == len(nums): 
                result.append(path[:])
                return 
            

            for i in range(len(nums)): 

                if used[i]: 
                    continue 
                
                used[i] = True 
                path.append(nums[i])

                backtrack(path)

                path.pop()
                used[i] = False
            
        backtrack([])
        return result





# goal: output all permutaitons (order matters)
    # all num in nums must be used 


# base case:
    # if len(path) == len(nums)
        # result.append(path[:])
        # return 


# consider duplicates 
    # for i in range(start, len(nums)): 
        # if i > start and candidates[i] == candidates[i-1]: 
            # continue 
        
        # path.append(candidates[i])
        # backtrack(i + 1, path, total + candidates[i])
        # path.pop()
        