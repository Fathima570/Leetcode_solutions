class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s

        n = len(s)
        half = n // 2

        left = sorted(s[:half])

        if n % 2 == 0:
            return "".join(left + left[::-1])
        else:
            return "".join(left + [s[half]] + left[::-1])
        
        