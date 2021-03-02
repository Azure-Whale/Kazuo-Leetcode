# 第一题：输入学生的ID和他上的课程，找到每两个学生上的相同的课程。
# 例如，输入{{"58", "A"},  {"94", "B"},  {"17", "A"},  {"58", "B"},  {"17", "B"},  {"58", "C"}}
# 输出:[58, 94]: [B]
#         [58, 17]: [A, B]
#         [94, 17]: []
# 第二题：给出一些课程和课程的先修课，每个课程有且只有一门先修课，并且保证学生只有一条path修完所有课程，求修到一半时的课程名称。
# 例如，输入{{A, B}, {C, D}, {B, C}, {E, F}, {D, E}, {F, G}}, 输出 D.
# 第三题: 第二题的follow up,假设每门课程可以有多门先修课,找出所有path修到一半课程的名称（出自其他面经）

# Time Complexity: O(E+V) E is the number of dependencies and V is the number of courses
# Space Complexity: O(E+V) 

q_input = [('A','B'),('C','D'),('B','C'),('E','F'),('D','E'),('F','G')]

# what's the header of the course path
all_cours = set()
cours_having_pre = set()

course_path = dict()

for x in q_input:
    pre,course = x
    all_cours.add(pre)
    all_cours.add(course)
    cours_having_pre.add(course)
    course_path[pre] = course

header_course = all_cours.difference(cours_having_pre).pop()
num_courses = len(q_input) + 1
# this is the middle index, if you want to get the real middle, it should be int((num_courses)+1/2)
middle_course = int((num_courses + 1)/ 2) 
cnt = 1
course = header_course
while True:
    if cnt == middle_course:
        print(course)
    cnt += 1
    if cnt == num_courses:
        break
    course = course_path[course]