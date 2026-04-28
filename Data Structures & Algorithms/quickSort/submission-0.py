# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair], s=None, e=None) -> List[Pair]:
        if s is e is None:
            s = 0
            e = len(pairs) - 1
        if e-s <=0:
            return pairs
        pivot = pairs[e].key
        left = s
        for i in range(s,e):
            if pairs[i].key < pivot:
                pairs[left], pairs[i] = pairs[i], pairs[left]
                left+=1
        pairs[e], pairs[left] = pairs[left], pairs[e]
        self.quickSort(pairs, s, left-1)
        self.quickSort(pairs, left+1, e)
        return pairs