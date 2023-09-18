from queue import PriorityQueue
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rs=[[sum(v),i] for i,v in enumerate(mat)]
        rs.sort()
        return [rs[i][-1] for i in range(k)]