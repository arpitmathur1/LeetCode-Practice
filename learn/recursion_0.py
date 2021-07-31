class Solution(object):
    
    def modify(self, s):
        if s == []:
            return []
        a = self.modify(s[1:])
        a.append( s[0] )
        return a
    
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        print(self.modify(s))

s = Solution()
s.reverseString(["H", "e", "l", "l", "o"])
