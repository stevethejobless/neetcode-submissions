class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int, ref_color=None) -> List[List[int]]:
        ROWS,COLS = len(image), len(image[0])
        if ref_color == None:
            ref_color = image[sr][sc]
        if (min(sr,sc) < 0 or sr == ROWS or sc == COLS or 
            color == image[sr][sc] or image[sr][sc] != ref_color):
            return image

        image[sr][sc] = color
        self.floodFill(image,sr+1,sc,color,ref_color)
        self.floodFill(image,sr,sc+1,color,ref_color)
        self.floodFill(image,sr,sc-1,color,ref_color)
        self.floodFill(image,sr-1,sc,color,ref_color)
        return image