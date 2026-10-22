class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        l, r = 0, len(people)-1
        while l<=r:
            if people[l] + people[r]<=limit:
                l = l+1
                r = r-1
            else:
                r=r-1
            boats = boats +1

        return boats