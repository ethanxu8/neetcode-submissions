class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        result = []

        def backtrack(start, path, total): 

            if total == target: 
                result.append(path[:])
                return 
            
            # stop early 
            if total > target: 
                return 

            # keep going 

            for i in range(start, len(candidates)):

                # skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return result




# base case 
    # if cur_sum == target: 
        # result.append(path[:])
        # return 

# decision 1: include nums[index]
    # cur_sum += nums[index]
    # path.append(nums[index])
    # backtrack (index + 1, path)
    # path.pop()


# decision: exclude nums[index]
    # backtrack (index + 1, path)
        


# goal: return all combinations that sum to target 
    # order of combinatiosn 
    # order of numbers in combinations do no matter


# each time we are checking if sum of candidates == target 

# Example 1
    # Input: candidates = [9,2,2,4,6,1,5], target = 8
    # Output: [ [1,2,5], [2,2,4], [2,6]]
    # 1 + 2 + 5 == 8, 2 + 2 + 4 == 8, 2 + 6 == 8 

# Example 2: 
    # 1 + 2 + 4 == 7 
    # 2 + 5 == 7 
    # 3 + 4 == 7 

# candidates = [1,2,3,4,5,6], target = x

    # start with first number 
    # 1 + 2 --> if 1 + 2 < target, keep going 
    # 1 + 2 > target, move on so 1 + 3 
    # if 1 + 2 == target, append to result 

# each time check if single candidate 
    # candidate > target immediately disregard it 