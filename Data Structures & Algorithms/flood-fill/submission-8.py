from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        orig_color = image[sr][sc]
        if orig_color == color:
            return image
        q = deque([(sr,sc)])
        image[sr][sc] = color
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c = q.popleft()
            print("POPLEFT",r,c)
            for i,j in dirs:
                nr,nc = r+i,c+j
                print(nr,nc)
                if 0<=nr<ROWS and 0<=nc<COLS and image[nr][nc] == orig_color:
                    q.append((nr,nc))
                    print(q)
                    image[nr][nc] = color
        return image 