class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        curr = [float("inf")] * (amount + 1)

        for i in range(amount + 1):
            if i % coins[0] == 0:
                curr[i] = i // coins[0]

        for i in range(1, len(coins)):
            temp = [float("inf")] * (amount + 1)

            for j in range(amount + 1):
                not_pick = curr[j]

                pick = float("inf")
                if coins[i] <= j:
                    pick = 1 + temp[j - coins[i]]

                temp[j] = min(pick, not_pick)

            curr = temp

        return -1 if curr[amount] == float("inf") else curr[amount]