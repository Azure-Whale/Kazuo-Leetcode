# 第一题：输入学生的ID和他上的课程，找到每两个学生上的相同的课程。
# 例如，输入{{"58", "A"},  {"94", "B"},  {"17", "A"},  {"58", "B"},  {"17", "B"},  {"58", "C"}}
# 输出:[58, 94]: [B]
#         [58, 17]: [A, B]
#         [94, 17]: []
# 第二题：给出一些课程和课程的先修课，每个课程有且只有一门先修课，并且保证学生只有一条path修完所有课程，求修到一半时的课程名称。
# 例如，输入{{A, B}, {C, D}, {B, C}, {E, F}, {D, E}, {F, G}}, 输出 D.


# 第三题: 第二题的follow up,假设每门课程可以有多门先修课,找出所有path修到一半课程的名称（出自其他面经）

q_input = [("58", "A"),("94", "B"),("17", "A"),("58", "B"),("17", "B"),("58", "C"),("3","C")]
# Time Complexity is O(n^2)
# Space Complexity is O(n)
map_course_student = dict()
student_ids = set()

for registeration in q_input:
    student_id, cours_id = registeration
    student_ids.add(student_id)
    map_course_student[cours_id] = map_course_student.setdefault(cours_id,set())
    map_course_student[cours_id].add(student_id)
student_ids = list(student_ids)
combos = []
ans = dict()

for i in range(len(student_ids)):   
    for j in range(i+1,len(student_ids)):
        combos.append((student_ids[i],student_ids[j]))

for course in map_course_student.keys():
    students = map_course_student[course]
    for combo in combos:
        ans[combo] = ans.setdefault(combo,[])
        if combo[0] in students and combo[1] in students:
            ans[combo].append(course)

print(ans)