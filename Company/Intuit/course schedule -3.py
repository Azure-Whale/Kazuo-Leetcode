# 第一题：输入学生的ID和他上的课程，找到每两个学生上的相同的课程。
# 例如，输入{{"58", "A"},  {"94", "B"},  {"17", "A"},  {"58", "B"},  {"17", "B"},  {"58", "C"}}
# 输出:[58, 94]: [B]
#         [58, 17]: [A, B]
#         [94, 17]: []
# 第二题：给出一些课程和课程的先修课，每个课程有且只有一门先修课，并且保证学生只有一条path修完所有课程，求修到一半时的课程名称。
# 例如，输入{{A, B}, {C, D}, {B, C}, {E, F}, {D, E}, {F, G}}, 输出 D.



# 第三题: 第二题的follow up,假设每门课程可以有多门先修课,找出所有path修到一半课程的名称（出自其他面经）

# Time Complexity is O(V^2)  Polynomial, as when I iterate each course, there could be (V-1) courses that I can contineu to iterate
# Space Complexity is O(V^2)  it has to store all possible pathes.
q_input = [('V','B'),('A','B'),('C','D'),('B','C'),('E','F'),('D','E'),('F','G'),('C','H'),('H','K'),('K','G'),('G','Z'),('Z','X'),('G','M'),('M','L')]
# a b c h k
all_cours = set()
cours_having_pre = set()

course_path = dict()

for x in q_input:
    pre,course = x
    all_cours.add(pre)
    all_cours.add(course)
    cours_having_pre.add(course)
    course_path[pre] = course_path.setdefault(pre,[])
    course_path[course] = course_path.setdefault(course,[])
    course_path[pre].append(course)

header_course = list(all_cours.difference(cours_having_pre))

#num_courses = len(q_input) + 1
# this is the middle index, if you want to get the real middle, it should be int((num_courses)+1/2)
# middle_course = int((num_courses + 1)/ 2) 1 2 3  3
def dfs(course, ans, path = []):
    path.append(course)
    if not course_path[course]:
        middle_number = int(((len(path) - 1)/2))
        ans.append([path,path[middle_number]])
        return 


    for cur in course_path[course]:
        temp_path = path.copy()
        dfs(cur,ans,temp_path)



headers = header_course
ans = []
for header in headers:
    print(header)
    dfs(header,ans)
print(ans)

    

# ans = set()
# def dfs(course,curr_index = 0):
#     if curr_index == 0:
#         course = header
    
#     try:
#         courses = course_path[course]
#     except KeyError:
#         print(curr_index)
#         return curr_index


#     for cour in courses:
#         length_path = dfs(cour,curr_index + 1)
#         if int((length_path-1)/2) == curr_index:
#             ans.add(cour)
    
#     return length_path

# dfs(header)

# print(ans)