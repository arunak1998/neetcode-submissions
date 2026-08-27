class TimeMap:

    def __init__(self):

        self.store={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:

            self.store[key]=[]

        self.store[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:

        res=""

        value=self.store.get(key,[])


        l=0
        r=len(value)-1

        while l<=r:

            mid=(l+r)//2


            if value[mid][1]<=timestamp:
                res=value[mid][0]

                l=mid+1
            else:
                r=mid-1

        return res
        
