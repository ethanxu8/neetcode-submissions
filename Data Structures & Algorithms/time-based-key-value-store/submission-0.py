class TimeMap:

    def __init__(self):
        self.library = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.library: 
            self.library[key] = []
        self.library[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.library.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r: 
            mid = (l + r) // 2
            if values[mid][1] <= timestamp: 
                res = values[mid][0]
                l = mid + 1
            else: 
                r = mid - 1
        
        return res



    # get 
    # Returns the most recent value of key if set was previously called on it and the most 
    # recent timestamp for that key prev_timestamp is less than or equal to the given timestamp
    #  If there are no values, it returns "".


    # cases to consider 
    # no values --> returns "" 
        # if self.library[key] 
    









    # Storing multiple values for the same key at specified time stamps
    # Retrieving the key's value at a specified timestamp
    
    # key : list of [value, timestampe] --> self.library = {}


    # set 
    # Stores the key key with the value value at the given time timestamp.

    # check if key is in self.library. if it is we add [value, timestampe]
    # if key is not in self.library, self.library[key] = [value, timestampe]


    





