class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        l = 0
        r = len(heights)-1
        while l<r:
            max_vol = max(max_vol, self.calculate_vol(l,r, heights))

            if heights[l] > heights[r]:
                r = r-1
            else:
                l = l+1
        return max_vol


    def calculate_vol(self, l,r, heights):
        return (r-l) * min(heights[l], heights[r])