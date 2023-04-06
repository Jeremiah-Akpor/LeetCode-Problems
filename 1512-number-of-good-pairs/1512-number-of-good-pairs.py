class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        """
        Given an integer array nums, return the number of good pairs.
        A pair (i,j) is called good if nums[i] == nums[j] and i < j.

        Args:
            nums (list[int]): An array of integers.

        Returns:
            int: The number of good pairs.

        Examples:
            >>> numIdenticalPairs([1, 2, 3, 1, 1, 3])
            4
            >>> numIdenticalPairs([1, 1, 1, 1])
            6
        """
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

