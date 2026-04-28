# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair], s=None, e=None) -> List[Pair]:
        print(s,e)
        if s is e is None:
            s = 0
            e = len(pairs) -1
        if e-s <= 0:
            return pairs
        
        m = (s+e)//2
        self.mergeSort(pairs, s, m)
        self.mergeSort(pairs, m+1, e)
        self.merge(pairs, s, m, e)
        return pairs
    
    def merge(self, pairs, s, m, e):
        L = pairs[s:m+1]
        R = pairs[m+1:e+1]
        i = j = 0
        k = s
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i+=1
            else:
                pairs[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            pairs[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            pairs[k] = R[j]
            j+=1
            k+=1


