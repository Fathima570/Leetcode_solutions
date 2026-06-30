class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)-len(needle)+1):
            new=''
            for j in range(len(needle)):
                if haystack[i+j]==needle[j]:
                    new+=haystack[i+j]
                else:
                    break
            if new==needle:
                return i
        return -1
        