class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s = 0
        c = len(matrix[0])
        r = len(matrix)
        e = r * c -1
        while s<=e:
            m = (s+e)//2
            if target > matrix[(m//c)][(m%c)]:
                s = m+1
            elif target < matrix[(m//c)][(m%c)]:
                e = m-1
            else: return True
        return False
        