class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() 
        result = [] 

        for right in range(len(nums)): 

            # check if q[-1] < nums[right] --> if it is then pop it and append 
            while q and nums[q[-1]] < nums[right]: 
                q.pop()

            q.append(right)

            if q[0] < right - k + 1: 
                q.popleft() 
            
            if right >= k - 1: 
                result.append(nums[q[0]])
        
        return result



        # right now our solution is too inefficient 
            # use a monotonic deqeue to keep track 




        # result = []

        # for left in range(len(nums) - k + 1):
        #     window = nums[left:left + k]
        #     result.append(max(window))

        # return result
        

        # call max_int in a for loop 
        # once right reaches end of nums then stop 


        # helper function max_sum which takes nums, k 


        # initalize a sliding window and then append max of each window 


        