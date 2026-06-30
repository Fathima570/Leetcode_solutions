class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i]==target:
                return i
                break
            elif target<nums[i]:
                return i
                break
        return len(nums)