class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        l = 0
        r = 1
        done = False
        swapping = False
        while not done:
            if nums[l]>nums[r]:
                temp = nums[r]
                nums[r] = nums[l]
                nums[l] = temp
                swapping = True
            if r==len(nums)-1:
                l=0
                r=1
                if swapping == False:
                    done = True
                swapping = False
            else:
                l=l+1
                r=r+1

# 210
# 120
# 102
# 012