class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points: 
            dist = -(x*x + y*y)
            heapq.heappush(heap, (dist, [x,y]))

            if len(heap) > k: 
                heapq.heappop(heap)
        
        
        
        return [point for _, point in heap]





# REACTO 

# min heap that keeps track of the k minimum euclidean dist points  


# Example 1: 
    # points = [[0,2],[2,2]], k = 1
    # [[0,2]]
    
    # find the euclidean distance using point (0,0) as (x2,y2)
    # the distance is put into a heap and you output heap[0:k]

# Example 2: process is the same 

# constraint: assume we do not need to consider the edge case 
    # k > number of points 

        