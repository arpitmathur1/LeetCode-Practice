# Find Common Characters
import collections

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = collections.Counter(words[0])
        for a in words:
            res &= collections.Counter(a)
        return list(res.elements())




s = Solution()
print(s.commonChars(["bella","label","roller"]))

"""
Runtime: 60 ms, faster than 41.98% of Python online submissions for Find Common Characters.
Memory Usage: 13.8 MB, less than 15.78% of Python online submissions for Find Common Characters.
"""