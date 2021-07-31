class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        print(height)
        max_area = 0
        l, r = 0, len(height)-1
        
        while l < r:
            area = min(height[l], height[r])*(r-l)
            if max_area < area:
                max_area = area
            
            if list[l] < list[r]:
                l += 1
            else:
                r -= 1
        print(max_area)
        return max_area


class Solution1(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                area = min(height[i], height[j]) * (j-i)
                if area > max_area:
                    max_area = area
        return max_area


t1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
s = Solution()
s.maxArea(t1)