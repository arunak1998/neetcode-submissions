class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False

            if board[i][j] != word[k] or visited[i][j]:
                return False

            if k == len(word) - 1:
                return True

            visited[i][j] = True

            found = (
                dfs(i + 1, j, k + 1) or
                dfs(i - 1, j, k + 1) or
                dfs(i, j + 1, k + 1) or
                dfs(i, j - 1, k + 1)
            )

            visited[i][j] = False

            return found

        visited=[[False] *len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):

            for j in range(len(board[0])):

                if board[i][j]==word[0]:
                    if dfs(i,j,0):
                        return True

        return False