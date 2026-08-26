class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        anagram={}

        for char in s:

            if char in anagram:
                 anagram[char]+=1
            else:
                anagram[char]=1
        for char in t:

            if char in anagram:
                 anagram[char]-=1
            else:
                anagram[char]=1
        return all(value == 0 for value in anagram.values())
        