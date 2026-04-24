class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))   
        cars.sort(reverse=True)

        stack = []

        for car in cars: 
            time = (target - car[0]) / car[1]

            if stack and time <= stack[-1]: 
                continue 
            else: 
                stack.append(time)
        return len(stack)




# Psuedocode 
# combine pos and speed, sort in descending order 

# traverse through cars and calculate time for each car
# if time of car <= prev car --> merge/collide, we continue 
# else we append it to stack 
# return len(stack) --> # of independent fleets

# traverse through cars once time comp O(n), space comp O(n)


# Approach: 
    # merge/collision problem --> each car in front has to keep track of the previous ccar
    # two possibilities --> either the car merges or it doesnt
    
    # fleet has to track any previous fleet --> prev unresolved issue --> car 

    # stack --> we dont need to track every element in the list we need to track the previous fleet/car
        # if the prev car will catch up, we ignore 
        # if the prev car cannot catch up, we append it to our stack as a sep fleet
        # return len(stack)

    # pos + speed --> go through every car and pos + speed each time until it reaches target
    # time = (target - pos) / speed --> each car calculated once 

    # we look from highest pos to lowest pos
    # sort cars (pos, speed)


        

# goal: return the # of fleets for cars reaching destination (target)

# Example 1: target -> 10, 1, 4
    # 1, 4 --> 4, 6, --> 7, 8 --> 10, 10 --> meet at 10, 1 fleet

# Example 2: target -> 10, 0, 1, 4, 7 resp. speeds 1, 2, 2, 1
    # note: position is not sorted --> 4 is the first pos in position not 0 
    # 1, 3, 6, 8 --> 2, 5, 8, 9 --> 3, 7, 10, 10 --> 3
