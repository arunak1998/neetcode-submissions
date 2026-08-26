class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res=[]
        for i in range(n+1):
            counter=0

            while i>1:

                if i & 1:

                    counter+=1

                i=i>>1

            if i==1:
                counter+=1
            res.append(counter)

        return res
