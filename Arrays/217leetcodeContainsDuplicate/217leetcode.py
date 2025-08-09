# https://leetcode.com/problems/contains-duplicate/submissions/1728711397/


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        s=set(nums)
        if len(nums)==len(s):
            return False
        return True
        
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i]==nums[i+1]:
        #         return True  
        # return False    