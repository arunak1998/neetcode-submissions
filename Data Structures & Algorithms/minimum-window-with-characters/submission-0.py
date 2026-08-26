class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t=="":
            return ""
        countT={}
        window={}

        for c in t:
            countT[c]=1+countT.get(c,0)

        have =0
        need=len(countT)


        l=0
        res=[-1,-1]

        reslen=float('inf')

        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)

            if c in countT and window[c]==countT[c]:
                have+=1


            while  need==have:

                if reslen >(r-l+1):
                    reslen=r-l+1

                    res=[l,r]

                window[s[l]]-=1
                c=s[l]
                if c in countT and window[c]<countT[c]:
                    have-=1

                l+=1

        l,r=res
        return s[l:r+1] if res !=float('inf') else ""

        






                


             
       
            
        