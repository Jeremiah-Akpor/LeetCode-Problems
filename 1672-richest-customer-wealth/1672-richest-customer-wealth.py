class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        m = len(accounts) -1
        a = m // 2 
        b = a +1
        x = 0
        for i in range(0,b):
            if not (b > m):
                x = max (x , sum(accounts[b]))
                b += 1
            x = max(x , sum(accounts[i]))
        return x
        