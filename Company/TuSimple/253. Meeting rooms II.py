# import heapq
# class Solution:
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         # Time : NlogN   Space:N
#         # key: use pq to get rooms having eailiest ending time, compare it with the starting time of current meeting, it doesn't. 
#         assigned_rooms = []
#         intervals = sorted(intervals,key=lambda x:x[0])
#         ans = 0
#         if not intervals:
#             return ans
#         heapq.heappush(assigned_rooms,intervals[0][1])
#         ans += 1

#         for i in range(1,len(intervals)):
#             # condition: when to free the room
#             if intervals[i][0] >= assigned_rooms[0]:
#                 heapq.heappop(assigned_rooms)
#             # when there is a new meeting, assigna new room
#             heapq.heappush(assigned_rooms,intervals[i][1])
#             ans = max(ans,len(assigned_rooms))
#         return ans
