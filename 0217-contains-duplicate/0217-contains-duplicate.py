class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_num = {}
        for num in nums:
            if num not in dict_num:
                dict_num[num] = 0
            dict_num[num] += 1
            if dict_num[num] > 1:
                return True
        return False