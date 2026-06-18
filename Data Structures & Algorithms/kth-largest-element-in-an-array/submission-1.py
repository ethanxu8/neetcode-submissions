class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums: 
            heapq.heappush(heap, num)

            if len(heap) > k: 
                heapq.heappop(heap)
        
        return heapq.heappop(heap)

# maintian a min heap of size k and then pop which is your answer 


# Example 1
    # nums = [2,3,1,5,4], k = 2
    # [1, 2, 3, 4, 5]
    # 2nd largest element which would be 4 

# heap --> max heap where for example 
    # if len(heap) 


# Example 2
    # nums = [2,3,1,1,5,5,4], k = 3
    # [1, 1, 2, 3, 4, 5, 5]
    # 3rd largest elment would be 4 


# result = []
    # append by popping of the heap 
    # once len(result) == k: return result[-1]


        