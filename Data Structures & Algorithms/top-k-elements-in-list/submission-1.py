class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums: 
            freq[num] = freq.get(num, 0) + 1
        
        return heapq.nlargest(k, freq, key=freq.get)



        # return the k most frequent elem in the arr 
            # k = 2, top 2 most frequent elements 
        # freq --> key:value pair, num:freq 
            # we can access the k highest numbers when it comes to freq 
        