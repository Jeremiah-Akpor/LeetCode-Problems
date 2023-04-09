class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        x = 0
        for account in accounts:
            x = max(x , sum(account))
        return x
        