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


        




        # make a stack with (pos, speed)


        # while loop -- cond while cars remain --> while position 

        # for pos in position: pos + speed 

        # if pos >= target, position.pop(pos), fleet += 1

        # need to mkae sure cars ant pass another car ahead of it
            # we need to track relative positions

            # one way is to sort position and then do if index higher but lower speed 




        # goal: return the number of fleets that reach the destination 

        # Example 
            # target 10, two cars at pos 1 and 4 
            # 1,4 --> 4,6 --> 7, 8 --< 10, 10, pos of car 1 and 2 meet at 10, 1 fleet 

            # target 10, four cars at pos 0, 1, 4, 7
            # 0,1,4,7 --> 1,3,6,8 --> 2,5,8,9 --> 3,7,10,10 --> 3 fleets
        

        # Approach 
        # update the pos of each car which is pos(car) + speed(car)
            # once new pos == pos of another car, fleet, make speed the same 
        
        # once pos reaches target we dont care about those cars, can pop them 
        # once all cars reach target return fleets
        