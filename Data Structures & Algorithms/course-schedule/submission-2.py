class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        premap={i:[] for i in range(numCourses)}

        for a,b in prerequisites:

            premap[a].append(b)

        visit=set()

        def dfs(crs):

            if crs in visit:
                return False


            if premap[crs]==[]:
                return True

            visit.add(crs)


            for pre in premap[crs]:

                if not dfs(pre): return False

            visit.remove(crs)

            premap[crs]=[]


            return True

        for crc in  range(numCourses):
            if not dfs(crc): return False 

        return True
            

            