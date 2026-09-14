class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        currmax, currmin = 1,1
        for n in nums:
            if n==0:
                currmin, currmax= 1,1
                continue
            tmpmax = n*currmax
            tmpmin = n*currmin
            currmax = max(n, tmpmax, tmpmin)
            currmin = min(n, tmpmax, tmpmin)
            res = max(res, currmax)

        return res        