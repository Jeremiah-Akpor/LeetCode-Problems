class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        hashtable = {}
        for num in nums:
            if num not in hashtable:
                hashtable[num] = 1
            else:
                hashtable[num] += 1

        ans = 0
        for value in hashtable.values():
            if value > 1 :
                ans += (value *(value - 1)) / 2
        return int(ans)

