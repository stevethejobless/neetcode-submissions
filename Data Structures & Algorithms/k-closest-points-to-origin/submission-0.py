import heapq,math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for pt in points:
            heapq.heappush(pq, (math.sqrt(pt[0]**2 + pt[1]**2),pt))
        output = []
        for i in range(0,k):
            output.append(heapq.heappop(pq)[1])
        return output