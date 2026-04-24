class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        s1_counter = Counter(s1)

        for i in range(len(s2) - len(s1) + 1): 
            window = s2[i:i+len_s1]
            if Counter(window) == s1_counter: 
                return True 
        return False
