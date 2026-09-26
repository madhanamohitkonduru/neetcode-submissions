class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l, sum = 0, 0
        count = float("inf")

        for r in range(len(nums)):
            sum = sum + nums[r]

            while sum>=target:
                count = min(r-l+1, count)
                sum = sum - nums[l]
                l = l+1

        return 0 if count==float("inf") else count
