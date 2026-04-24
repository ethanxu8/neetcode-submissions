class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0 
        max_length = 0 

        for r in range(len(s)): 

            # consider duplicates 
            while s[r] in char_set: 
                char_set.remove(s[l])
                l += 1
            
            # add new character to set 
            char_set.add(s[r])

            # update max_length 
            max_length = max(max_length, r - l + 1)
        
        return max_length

        
        # if not s return 0 --> edge case

        # for i in range(1, len(s))
        # max_length initialize at 1 
        # add s[i] to a list 
        # if the next one is not in the list increment max_length by 1 



        # have a window that expands if the string is not the same and if same restarts 
