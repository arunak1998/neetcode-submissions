
import re
class Solution:
    

        
    def isPalindrome(self, s: str) -> bool:
        
        s=s.strip().replace(" ","").lower()
        pattern = r'[^a-z0-9]'  # Regex pattern to match non-alphanumeric characters
        s = re.sub(pattern, '', s)
        print(s)
        def check(s,i,j):
            if i>=j:
                return True
            if s[i]!=s[j]:
                return False
           

            return check(s,i+1,j-1)

        return check (s,0,len(s)-1)
