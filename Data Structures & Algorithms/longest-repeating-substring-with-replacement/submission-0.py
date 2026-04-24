class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {} # hashmap with char:freq key value pairs
        l = 0 # initialize a left pointer
        max_freq = 0 # max number of same characters
        max_length = 0 # max length including k replacements

        for r in range(len(s)): 
            freq[s[r]] = freq.get(s[r], 0) + 1

            max_freq = max(max_freq, freq[s[r]]) # update max_freq value 

            # when window size (r - l + 1) - max_freq > k 
            while (r - l + 1) - max_freq > k: 
                # shrink window size 
                freq[s[l]] -= 1
                l += 1
            
            max_length = max(max_length, r - l + 1)
        
        return max_length