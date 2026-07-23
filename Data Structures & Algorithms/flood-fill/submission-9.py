class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ori = image[sr][sc]
        ROWS = len(image)
        COLS = len(image[sr])
        visit = set()
        if ori == color:
            return image
        def dfs(image,sr,sc,color):
            nonlocal ori
            nonlocal visit
            nonlocal ROWS
            nonlocal COLS
            if min(sr,sc) < 0 or sr == ROWS or sc == COLS or (sr,sc) in visit or image[sr][sc]!=ori:
                return image
            elif image[sr][sc] == ori:
                image[sr][sc] = color
            visit.add((sr,sc))
            dfs(image,sr+1,sc,color)
            dfs(image,sr,sc+1,color)
            dfs(image,sr-1,sc,color)
            dfs(image,sr,sc-1,color)

        dfs(image,sr,sc,color)
        return image