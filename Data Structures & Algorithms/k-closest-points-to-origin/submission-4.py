import heapq,math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for pt in points:
            pq.append((pt[0]*pt[0]+pt[1]*pt[1],pt))
        heapq.heapify(pq)
        output = []
        for i in range(0,k):
            output.append(heapq.heappop(pq)[1])
        return output