class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        amounts = [0] * (amount+1)
        amounts[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                amounts[i] = amounts[i] + amounts[i-coin]
        return amounts[-1]