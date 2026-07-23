class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[sr])
        ori = image[sr][sc]
        if ori == color:
            return image
        stack = [(sr,sc)]
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        while stack:
            r,c = stack.pop()
            if 0 <= r < ROWS and 0 <= c < COLS and image[r][c] == ori:
                image[r][c] = color
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and image[nr][nc] == ori:
                        stack.append((nr, nc))
        return image