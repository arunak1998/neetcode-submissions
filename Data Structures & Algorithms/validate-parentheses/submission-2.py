class Solution:
    def isValid(self, s: str) -> bool:

        paren_map={')':'(','}':'{',']':'['}

        stack=[]
        for char in s:
            if char  in paren_map:
                if stack and stack[-1]==paren_map[char]:
                    stack.pop()

                else:
                    return False

            else:
                stack.append(char)
        return True if not stack else False

