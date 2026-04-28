# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        
        m = len(pairs)//2
        left = self.mergeSort(pairs[:m])
        right = self.mergeSort(pairs[m:])

        return self.merge(left,right)

    def merge(self,left,right):
        i = j = 0
        arr = []
        while i<len(left) and j<len(right):
            if left[i].key <= right[j].key:
                arr.append(left[i])
                i+=1
            else:
                arr.append(right[j])
                j+=1
        while i < len(left):
            arr.append(left[i])
            i+=1
        while j < len(right):
            arr.append(right[j])
            j+=1
        return arr
