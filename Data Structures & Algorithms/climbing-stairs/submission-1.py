class Solution:
    def climbStairs(self, n: int) -> int:
        lis = [0, 1, 2]
        if n==2:
            return 2
        if n==1:
            return 1
        for i in range(3,n+1):
            lis.append(lis[i-1]+lis[i-2])
        return lis.pop()