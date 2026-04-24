class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # return first 
        if len(tokens) <= 2: 
            return int(tokens[0])


        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        stack = []
        for token in tokens: 
            if token not in ops: 
                stack.append(int(token))
            else: 
                b = stack.pop()
                a = stack.pop()
                res = ops[token](a,b)
                stack.append(res)
        return res



        
        



       

        


        # goal: output int which is the result of token calculations 

        # Example 1: tokens = ["1","2","+","3","*","4","-"]
            # - 
            # ((1 + 2) * 3) - 4
        
        # nums1, nums2, exp
        # nums1 = 1, nums2 = 2, exp = + 
        # res = nums1 exp nums2
        # makes nums1 = res
        # then nums2, then exp 
        # do that until exp reaches end of list 



        