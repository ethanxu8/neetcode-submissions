class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites: 
            preMap[crs].append(pre)
        
        visitSet = set()
        doneSet = set()

        def dfs(crs): 
            # cycle check 
            if crs in visitSet: 
                return False 
            
            # already completed 
            if crs in doneSet: 
                return True

            visitSet.add(crs)
        
            for pre in preMap[crs]: 
                if not dfs(pre): 
                    return False

            visitSet.remove(crs)
            
            doneSet.add(crs)

            result.append(crs)

            return True
        
        for crs in range(numCourses): 
            if not dfs(crs): 
                return []
        return result





# if a cycle is detected return []

# else, for crs, pre in prerequisites append pre then crs 
        