#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : course schadule.py
@Time    : 2/14/2021 4:41 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''
courses = [(0, 1), (2, 3), (4, 5), (1, 2), (5, 0), (6, 4)]

num_courses = len(courses)
courses_index = {}
known = set()
nxts = set()

for p in courses:
    prevCourse, nextCourse = p
    courses_index[prevCourse] = courses_index.setdefault(prevCourse, nextCourse)
    known.add(prevCourse)
    known.add(nextCourse)
    nxts.add(nextCourse)

head = known.difference(nxts).pop()

middle_course = int(num_courses - 1 / 2)

cnt = 0
ans = []
last_course = None
print(head)
for i in range(num_courses):
    if not last_course:
        last_course = head

    curr_course = courses_index[last_course]
    last_course = curr_course

    if i == int(num_courses - 1 / 2):
        ans.append(curr_course)
print(ans)