class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        print(people)
        l, r = 0, len(people)-1
        while l<=r:
            print(l, r)
            if people[l] + people[r]<=limit:
                boats = boats +1
                l = l+1
                r = r-1
            else:
                boats = boats+1
                r=r-1

        return boats