class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s_i = 0
        e_i = len(matrix) -1
        s_j = 0
        e_j = len(matrix[0]) -1
        while s_i <= e_i:
            m_i = (s_i+e_i)//2
            if target > matrix[m_i][e_j]:
                s_i = m_i + 1
            elif target < matrix[m_i][s_j]:
                e_i = m_i - 1
            else:
                return self.binary_search(matrix[m_i],target)
        return False
    
    def binary_search(self,arr,target):
        s = 0
        e = len(arr) -1
        while s<=e:
            m = (s + e)//2
            if target > arr[m]:
                s = m + 1
            elif target < arr[m]:
                e = m -1
            else: return True
        return False