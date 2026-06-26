class Solution(object):
    def removeDuplicates(self, nums):
        rem=[]
       
        for i in nums:
            if i not in rem:
                rem.append(i)
           
        for n in range(len(rem)):
            nums[n]=rem[n]
        return len(rem)
        
        

        