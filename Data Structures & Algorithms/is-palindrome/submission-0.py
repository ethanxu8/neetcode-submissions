class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''
        for char in s: 
            if char.isalnum():
                cleaned += char.lower()

# use two pointers 

        left = 0 
        right = len(cleaned) - 1

        while left < right: 
            if cleaned[left] != cleaned[right]: 
                return False 
            left += 1
            right -= 1

        return True

        

# normalize string 
    # remove spaces .isalnum() function to remove spaces and keep only alphabetical characters
    # .lower() function to lower alphabetical characters 

# use two pointers to check if the charactes are the same
# if not return false, if it yes return true 

