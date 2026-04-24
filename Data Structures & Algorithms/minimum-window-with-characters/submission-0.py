class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case: if len(t) > len(s), output ""
        if len(t) > len(s): 
            return ""
        
        # freq map for t: what we need to satisfy 
        need = {}
        for i in range(len(t)):
            need[t[i]] = need.get(t[i], 0) + 1 

        window = {} # freq map for window 
        have = 0 # how many 
        need_count = len(need) # conditions that we need to satisfy

        res = [-1, -1]
        res_len = float('inf')
        l = 0 

        for r in range(len(s)): 
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in need and window[s[r]] == need[s[r]]: # checking freq
                have += 1
            
            while have == need_count: 
                if (r - l + 1) < res_len: 
                    res = [l, r]
                    res_len = r - l + 1

                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]: 
                    have -= 1
                l += 1
            
        l,r = res
        return s[l:r+1] if res_len != float("inf") else ""
        


        

        # condition where it looks for all char in t
       
        # everytime you hit a char in s you decrease freq by one until all freq are 0
        # start tracking when you hit the first one 



