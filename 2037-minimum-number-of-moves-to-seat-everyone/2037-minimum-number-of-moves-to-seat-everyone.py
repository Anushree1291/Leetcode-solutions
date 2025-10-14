class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        a=sorted(seats)
        b=sorted(students)
        return sum( abs(i -j ) for i ,j in zip(a,b) )