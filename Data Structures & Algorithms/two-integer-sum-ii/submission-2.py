class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(numbers)): 
            lookup = target - numbers[i]
            if lookup in hashmap: 
                return [hashmap[lookup] + 1, i + 1]
            else: 
                hashmap[numbers[i]] = i

        # number : index 

        # hashmap that shows the index:number
        # target - element and check if it is in hashmap
        # if no add it to the hashmap 
        # if yes return the two indicies
        