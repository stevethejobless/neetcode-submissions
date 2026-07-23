from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS,COLS = len(image), len(image[sr])
        ori = image[sr][sc]
        if ori == color:
            return image
        moves = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque([(sr,sc)])
        while q:
            r,c = q.popleft()
            if 0<=r<ROWS and 0<=c<COLS and image[r][c] == ori:
                image[r][c] = color
                for move in moves:
                    nr,nc = move
                    q.append((r+nr,c+nc))
        return image