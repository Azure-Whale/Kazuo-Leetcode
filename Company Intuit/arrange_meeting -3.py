"""
第一题：类似meeting rooms，输入是一个int[][] meetings, int start, int end, 每个数都是时间，13：00 =》 1300， 9：30 =》 930， 看新的meeting 能不能安排到meetings
ex: {[1300, 1500], [930, 1200],[830, 845]}, 新的meeting[820, 830], return true; [1450, 1500] return false;
insert interval and check to see if you can find any overlap 

第二题：类似merge interval，唯一的区别是输出，输出空闲的时间段，merge完后，再把两两个之间的空的输出就好，注意要加上0 - 第一个的start time
第三题：是给会议分配房间。已知每个会议的人数、开始时间、结束时间，以及每个房间的容量。
输入：
    会议列表：每个会议有名称、人数、开始时间、结束时间
    房间列表：每个房间有名称、容量。.
   
    输出：
    每个会议安排在哪个房间，格式是“会议名:房间名”
    如果没法都安排，输出"impossible"
"""

# Time Complexity O(n*m)
# Sapce Complexity O(n) where n is the length of given input

meetings = [[1300, 1500,3], [930, 1200,5],[830, 845,4]]
meeting_rooms = [['Large',5],['Medium',4],['Small',3]]

import heapq
def assign_rooms(meetings, meeting_rooms):
    # Time Complexity O(n*m)
    # Sapce Complexity O(n) where n is the length of given input
    ans = []
    # I would sort them for further processing
    meeting_rooms = sorted(meeting_rooms,key=lambda x:x[1]) # by room size
    meetings = sorted(meetings,key=lambda x:x[2]) # by meeting size
    meetings = sorted(meetings,key=lambda x:x[0]) # by meeting starting time
    # build a dictionary to mark the availabity of the rooms
    meeting_room_status = dict()
    # init the room status init, key is the room name
    for room in meeting_rooms:
        meeting_room_status[room[0]] = 1

    used_rooms = []
    # need to know when the room will be free, use a min-heap to store the availbity of rooms, the weight the ending time of the meeting that occupied this room
    assigned = False
    # assign the first meeting, if it unavailble, return false
    for room in meeting_rooms:
        assigned = False
        if room[1]>=meetings[0][2] and meeting_room_status[room[0]] == 1:
            heapq.heappush(used_rooms,(meetings[0][1],room[0]))
            meeting_room_status[room[0]] = 0
            assigned = True
            break
    if not assigned:
        return 'impossible'
    # iterate the meeting
    for meeting in meetings[1:]:
        # if there are used rooms, the meeting starting time is later than the ending time of the running meeting,
        while used_rooms and meeting[0] >= used_rooms[0][0]:
            temp = heapq.heappop(used_rooms)
            ans.append(['meeting_name',temp[0],temp[1]])
            meeting_room_status[temp[1]] = 1
        # check if we can assign it
        assigned = False
        for room in meeting_rooms:
            if room[1]>=meeting[2] and meeting_room_status[room[0]] == 1:
                heapq.heappush(used_rooms,(meeting[1],room[0]))
                meeting_room_status[room[0]] = 0
                assigned = True
                break
        if not assigned:
            print(used_rooms)
            print(meeting)
            return 'impossible'
    # clear the used rooms
    while used_rooms:
        temp = heapq.heappop(used_rooms)
        ans.append(['meeting_name',temp[0],temp[1]])
    return ans
            



print(assign_rooms(meetings,meeting_rooms))