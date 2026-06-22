class Solution:
    r = list()
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1,0,1,2,-1,-4]
        # -1 
        hash = {}
        
        for i in range(0, len(nums)-2, 1):
            l = i+1
            r = len(nums)
            nums2 = nums[l:r]
            self.r = self.r + self.twosum(nums2, nums[i]*-1)
        return list({tuple(sorted(item)): item for item in self.r}.values())
            
            
        

    def twosum(self, nums2, target):
        lis = {}
        r = list()
        for i, n in enumerate(nums2):
            diff = target - n
            if diff in lis:
                r.append([diff, n, target*-1])
            lis[n] = i
        return r