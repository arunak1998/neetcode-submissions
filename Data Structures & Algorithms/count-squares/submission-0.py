class CountSquares:

    def __init__(self):
        self.ptsmap=defaultdict(int)
        self.pts=[]

    def add(self, point: List[int]) -> None:

        self.ptsmap[tuple(point)]+=1

        self.pts.append(point)
        

    def count(self, point: List[int]) -> int:

        res=0

        px,py=point

        for x ,y in self.pts:

            if abs(py-y)!=abs(px-x) or px==x or py==y:
                continue

            res+=self.ptsmap[(x,py)]*self.ptsmap[(px,y)]

        return res
        
