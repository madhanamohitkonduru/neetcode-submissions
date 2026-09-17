class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        maps = {}
        for i in s1:
            maps[i] = 1+maps.get(i, 0)
        l, r = 0, 0
        maps2 = maps.copy()
        while r<len(s2):
            if s2[r] in maps2:
                maps2[s2[r]] = maps2[s2[r]] -1
                if maps2[s2[r]] <=0:
                    maps2.pop(s2[r])
                if len(maps2) <=0:
                    return True
                r = r+1
            else:
                l = l+1
                r = l
                maps2 = maps.copy()

        return False