class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        path = []

        def dfs(i):
            if i == len(digits):
                result.append("".join(path))
                return

            for j in range(len(chars[digits[i]])):
                path.append(chars[digits[i]][j])
                dfs(i + 1)
                path.pop()

        dfs(0)
        return result
