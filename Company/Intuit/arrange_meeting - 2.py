"""
第一题：类似meeting rooms，输入是一个int[][] meetings, int start, int end, 每个数都是时间，13：00 =》 1300， 9：30 =》 930， 看新的meeting 能不能安排到meetings
ex: {[1300, 1500], [930, 1200],[830, 845]}, 新的meeting[820, 830], return true; [1450, 1500] return false;
insert interval and check to see if you can find any overlap 

第二题：类似merge interval，唯一的区别是输出，输出空闲的时间段，merge完后，再把两两个之间的空的输出就好，注意要加上0 - 第一个的start time
第三题：是给会议分配房间。已知每个会议的人数、开始时间、结束时间，以及每个房间的容量。
输入：
    会议列表：每个会议有名称、人数、开始时间、结束时间
    房间列表：每个房间有名称、容量。.本文原创自1point3acres论坛
   
    输出：
    每个会议安排在哪个房间，格式是“会议名:房间名”
    如果没法都安排，输出"impossible"
"""

# Tiem Complexity is O(nlogn)
# Space Complexity is O(n) where is number of meeting

meetings = [[0,40],[1300, 1500], [930, 1200],[830, 845]]
new_meeting = [1450,1600]

def get_spare_time(meetings, new_meeting):

    meetings.append(new_meeting)

    meetings = sorted(meetings, key = lambda x:x[0])
    new_meeting = []
    spare_time = []
    if len(meetings)<=1:
        pass

    start_time = meetings[0][0]
    end_time = meetings[0][1]

    for i in range(len(meetings)-1):
        # if the end time is larger or equal to the start meeting of next meeting
        if end_time>=meetings[i+1][0]:
            # update it if larger than the ending time
            end_time = end_time if end_time>=meetings[i+1][1] else meetings[i+1][1]
        else:
            new_meeting.append([start_time,end_time])
            start_time = meetings[i+1][0]
            end_time = meetings[i+1][1]
    new_meeting.append([start_time,end_time])
    
    start = 0
    for i in range(len(new_meeting)):
        if new_meeting[i][0]==0:
            start = new_meeting[i][1]
            continue
        if start<new_meeting[i][0]:
            spare_time.append([start,new_meeting[i][0]])
            start = new_meeting[i][1]
    return spare_time


print(get_spare_time(meetings,new_meeting))