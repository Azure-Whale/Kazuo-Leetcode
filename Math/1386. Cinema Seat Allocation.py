from collections import defaultdict
#https://leetcode.com/problems/cinema-seat-allocation/

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        #by defualy, 
        res = 2*n
        
        seats = defaultdict(lambda:[0,0,0])

        for i,j in reservedSeats:
            if j in {2,3,4,5}:
                seats[i][0] = 1
            if j in {4,5,6,7}:
                seats[i][1] = 1
            if j in {6,7,8,9}:
                seats[i][2] = 1
        cnt = 0
        for row in seats:
            row_seat = seats[row]
            if row_seat[0] == 1 and row_seat[2] == 1:
                if row_seat[1] == 0:
                    cnt += 1
            elif row_seat[0] == 0 and row_seat[2] == 0:
                cnt += 2
            else:
                cnt += 1
        
        
        return (n - len(seats))*2 + cnt