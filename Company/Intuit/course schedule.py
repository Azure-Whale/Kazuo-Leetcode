#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : course schedule.py
@Time    : 2/18/2021 3:11 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''
"""
第一题：输入学生的ID和他上的课程，找到每两个学生上的相同的课程。
例如，输入{{"58", "A"},  {"94", "B"},  {"17", "A"},  {"58", "B"},  {"17", "B"},  {"58", "C"}}
输出:[58, 94]: [B]
        [58, 17]: [A, B]
        [94, 17]: []
第二题：给出一些课程和课程的先修课，每个课程有且只有一门先修课，并且保证学生只有一条path修完所有课程，求修到一半时的课程名称。
例如，输入{{A, B}, {C, D}, {B, C}, {E, F}, {D, E}, {F, G}}, 输出 D.
第三题: 第二题的follow up,假设每门课程可以有多门先修课,找出所有path修到一半课程的名称
"""

