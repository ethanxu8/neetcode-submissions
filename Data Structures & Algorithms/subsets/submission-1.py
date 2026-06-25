class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        def backtrack(index, path): 

            # base case 
            if index == len(nums): 
                result.append(path[:])
                return 

            # case 1: include the number 
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            # case 2: skip the number 
            backtrack(index + 1, path)
        
        backtrack(0, [])
        return result
        