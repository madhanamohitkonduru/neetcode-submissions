class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lis1=[1] * len(nums)
        lis2=[1] * len(nums)
        for i in range(1,len(nums)):
            lis1[i]= lis1[i-1] * nums[i-1]
        print(lis1)

        for i in range(len(nums)-2,-1,-1):
            lis2[i] = lis2[i+1] * nums[i+1]
        print(lis2)
        
        return [lis1[i]* lis2[i] for i in range(len(nums))]