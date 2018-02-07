class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxReach = nums[0]
        for i, num in enumerate(nums):
            if maxReach < i:
                return False
            if maxReach >= len(nums) - 1:
                return True
            maxReach = max(maxReach, num + i)
        return False
