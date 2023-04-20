class Solution:
    def floodFill(self, i: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def tra(r,c, no,co):
            if i[r][c]==no  :
                i[r][c]=co
                if(r>=1): tra(r-1,c,no,co)
                if(c>=1): tra(r,c-1,no,co)
                if(r<len(i)-1): tra(r+1,c,no,co)
                if(c<len(i[0])-1): tra(r,c+1,no,co)
        
        if(i[sr][sc]!=color):
            tra(sr,sc,i[sr][sc],color)
        
        return i