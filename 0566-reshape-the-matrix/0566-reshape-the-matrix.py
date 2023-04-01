import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        a=len(mat)*len(mat[0])
        if(a==r*c):
            return np.reshape(mat,(r,c))
        else:
            return mat