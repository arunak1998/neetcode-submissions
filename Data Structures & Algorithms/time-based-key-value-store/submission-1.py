class TimeMap:

    def __init__(self):
        self.store={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        
        result=''
        values=self.store.get(key,[])
        l=0
        h=len(values)-1

        while(l<=h):
            mid=(l+h)//2

            if values[mid][1]<=timestamp:
                result=values[mid][0]
                l=mid+1
            else:
                h=mid-1
        return result
