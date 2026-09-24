class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for x,y in points:
            dist.append((- (x**2 + y**2), [x, y]))

        heapq.heapify(dist)
        while len(dist) > k:
            heapq.heappop(dist)
        
        return [pt for _, pt in dist]