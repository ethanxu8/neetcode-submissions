class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }


        if digits == "": 
            return []
        
        def backtrack(index, path): 
            if index == len(digits): 
                result.append("".join(path))
                return
            
            digit = digits[index]

            for letter in phone[digit]: 
                path.append(letter)
                backtrack(index+1, path)
                path.pop()
        
        backtrack(0, [])
        return result


        


# edge case 
    # if digits = "" then output []

# base case once index == len(str)
    

# digit ==> string 
# 2 ==> "abc"
    # base case --> once index reached len(str)-1, then you're done

# you have to alternate from each digit 
    # in the case of 34 
    # 00, 01, 10, 11
        