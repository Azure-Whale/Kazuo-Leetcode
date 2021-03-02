#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : intuit_OA.py
@Time    : 2/14/2021 5:31 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''
# https://www.1point3acres.com/bbs/thread-696992-1-1.html

max_len = 12
# text = ['It was the best',
#         'of times it was',
#         'the worst of times']
text = ['Itaaaaa was the best',
        'of times it was',
        'the worst of times']
words = []
for line in text:
    w = line.split()
    for _ in w:
        words.append(_)

ans_text = []
curr_letter = 0
num_words = 0
lines = []
line = []
for i in range(len(words)):
    # if there are suffix
    if num_words != 0:
        temp_length = len(words[i]) + curr_letter + num_words
        # added?
        if temp_length <= max_len and ((max_len - (len(words[i]) + curr_letter)) % num_words == 0):
            line.append(words[i])
            num_words += 1
            curr_letter += len(words[i])
        # if cannot, finish this line and init all relevant parameters and add it to next line
        else:
            if num_words>1:
                space_length = int((max_len - curr_letter)/(num_words-1))
                lines.append(('-' * space_length).join(line))
            else:
                lines.append(line[0]+'-'*(max_len-curr_letter))
            line = []
            line.append(words[i])
            num_words = 1
            curr_letter = len(words[i])
    # if the line is empty
    else:
        line.append(words[i])
        num_words = 1
        curr_letter = len(words[i])
    if i == (len(words) - 1):
        if num_words > 1:
            space_length = int((max_len - curr_letter) / (num_words - 1))
            lines.append(('-' * space_length).join(line))
        else:
            lines.append(line[0] + '-' * (max_len - curr_letter))
