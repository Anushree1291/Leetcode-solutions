class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        a=sorted(seats)
        b=sorted(students)
        c=0
        for i in range(len(a)):
            c+= abs(a[i]-b[i])
        return c