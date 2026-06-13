class Solution(object):
    def isPalindrome(self, x):
        rev=0
        x1=x
        while x>0:
            dig=x%10
            rev=rev*10+dig
            x=x//10
        if x1==rev:
            return True
        else:
            return False

    