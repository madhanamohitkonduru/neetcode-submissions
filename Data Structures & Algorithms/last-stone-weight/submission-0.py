class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-1 * i for i in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap)>1:
            first = heapq.heappop(maxHeap) * -1
            second = heapq.heappop(maxHeap)* -1
            new = first - second
            if new !=0:
                heapq.heappush(maxHeap, new * -1)

        return heapq.heappop(maxHeap)* -1 if len(maxHeap)==1 else 0
