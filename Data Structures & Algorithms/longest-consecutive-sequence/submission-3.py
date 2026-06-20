class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 2, 20, 4, 10, 3, 4, 5
        # 1, 19, 3, 9 , 2, 3, 4
        # f, f,  t, f,  t, t, t

        if len(nums) == 0:
            return 0

        before = []
        is_there = []
        for i in nums:
            if i-1 not in nums:
                is_there.append(i)

        print(is_there)
        
        c = 1
        mc = 1
        for i in is_there:
            j = i
            while True:
                if j+1 in nums:
                    c += 1
                    j += 1
                else:
                    break
            mc = max(c, mc)
            c = 1
        return mc