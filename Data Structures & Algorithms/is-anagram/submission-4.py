class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
        # freq of char match, order does not matter 
            # sort --> O(nlogn)
            # freq --> hashmap or ascii, two for loops --> O(n) + O(n)
        # if s and t are diff lengths, return False 