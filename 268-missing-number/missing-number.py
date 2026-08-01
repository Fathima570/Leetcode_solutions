class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)+1
        l=list(range(0,n))
        nums.sort()
        for i in range(n):
            if l[i] not in nums:
                return l[i]
        
            

        

        