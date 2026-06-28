class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return min(nums[0], nums[1])
        mid = len(nums)//2
        print (nums[mid])
        l = mid-1
        r = mid + 1

        while nums[mid]>=nums[l] or nums[mid]>=nums[r]:
            if nums[l]<nums[mid]:
                if l==0:
                    l = len(nums)-1
                else:
                    l = l-1
                mid = mid - 1
                r = r - 1
            else:
                l = l+1
                mid = mid +1
                if r == len(nums)-1:
                    r = 0
                else:
                    r = r+ 1
        return nums[mid]