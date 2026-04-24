class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # flattened list of values in the 2d matrix 
        flat = [val for row in matrix for val in row]

        left, right = 0, len(flat) - 1

        while left <= right: 
            mid = (left + right) // 2
            if flat[mid] == target: 
                return True 
            elif flat[mid] >= target: 
                right = mid - 1
            else: 
                left = mid + 1
        
        return False

        




        # make the 2d matrix a list of values 

        # then normal binary search 







        # 00 01 02 03 10 11 12 13 20 

        # once the right hand numebr reaches len(list) - 1 increment the left one 
        # once you reach len(list), len(list) end the loop


        # left = [0,0]
        # right = [len(matrix), len(marix[])]


        # 00 len(list), len(list)
        