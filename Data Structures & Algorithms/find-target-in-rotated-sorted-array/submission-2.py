class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: 
            m = (l + r) // 2
            if nums[m] == target: 
                return m 
            
            # left half is sorted 
            if nums[l] <= nums[m]: 
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else: 
                    l = m + 1
            # right half is sorted
            else: 
                if nums[m] < target <= nums[r]: 
                    l = m + 1
                else: 
                    r = m - 1
        
        return -1

        # have left and right pointers 
        # have middle
        # it should always be ascending even if rotated so 
        
        # if nums[l] < nums[r] it means its sorted 
            # if target > middle then make l = m + 1
            # if target < middle then make r = m - 1
            # target == middle return index 
        
        # if nums[l] <= nums[m] then left half is sorted
            # if nums[l] <= target < nums[m] then r = m - 1
            # else l = m + 1
        # else right is sorted 
            # if nums[m] < target <= nums[r] then l = m + 1
            # else r = m - 1


        # binary search 