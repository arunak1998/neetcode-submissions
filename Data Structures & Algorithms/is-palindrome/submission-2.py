class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # def check(i,j):

        #     if i > j:
        #         return True

        #     if s[i]!=s[j]:
        #         return False

        #     check(i+1,j-1)

        # return check(0,len(s)-1)

      


        i=0
        j=len(s)-1
        while i<j:
           
            while i < j and not s[i].isalnum():
                i += 1

            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False

            i+=1
            j-=1
        return True

