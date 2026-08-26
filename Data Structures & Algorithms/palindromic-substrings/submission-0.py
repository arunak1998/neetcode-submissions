class Solution:
    def countSubstrings(self, s: str) -> int:

        def palindrome(a):

            if a==a[::-1]:

                return True
            return False

            
        
        def ispalindrome(i,count):

            if i==len(s):

                return count
            for end in range(i, len(s)):
                if palindrome(s[i:end+1]):  # Check if the substring is a palindrome
                    count += 1


        

            return ispalindrome(i+1,count)
        return ispalindrome(0,0)


            