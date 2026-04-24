class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        tot_prod = 1
        zeros = 0 
        res = []

        for num in nums: 
            if num == 0: 
                zeros += 1
            else: 
                tot_prod *= num
        
        # two or more zeros
        if zeros > 1: 
            return [0] * len(nums)


        # division without zero 
        for num in nums: 
            if zeros == 1: 
                if num == 0: 
                    res.append(tot_prod)
                else: 
                    res.append(0)
            else: 
                res.append(tot_prod // num)
        
        return res


        # no zeros -- current code works 
        # 1 zero -- index with zero gets prod without 0 
        # 2 zeros -- everything becoems 0 
    


        # we can find the total product and divide by num in nums
            # product / 0 --> undefined error 
            # edge case: if num == 0, change 0 to 1 and find product 

        # prod of the array excluding num in nums for all nums
            # output a list of respective products 
        
        # 0: makes every product 0 except for when we exclude it 
        