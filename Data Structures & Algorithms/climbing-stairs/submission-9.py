class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        lis = [0,1, 2]
        for i in range(3,n+1):
            lis.append(lis[i-1]+lis[i-2])
        return lis.pop()