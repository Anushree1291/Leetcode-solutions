class Solution:
    def isValidSudoku(self, b: List[List[str]]) -> bool:
        
        def back(b,i,j,ch)->bool:
            for x in range(j+1,len(b)):
                if(b[i][x]==ch):
                    return False
            for x in range(i+1,len(b)):
                if(b[x][j]==ch):
                    return False
            r=i-i%3
            c=j-j%3
            for x in range(r,r+3):
                for y in range(c,c+3):
                    if(b[x][y]==ch and (x is not i) and (y is not j)):
                        return False
            return True
        
        
        for i in range(9):
            for j in range(9):
                if b[i][j] is not ".":
                    c=back(b,i,j,b[i][j])
                    if(c==False):
                        return False
        return True
    
        
        
        
        