#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : intuit_iterate_tree.py
@Time    : 2/13/2021 5:33 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''


with open('input', 'r') as read_input:
    pairs = read_input.readlines()
    pairs = [x.strip() for x in pairs]


def dfs(node, end_point):
    if not node.next:
        end_point.add(node.value)

    for nd in node.next:
        dfs(nodes[nd.value], end_point)


class Node(object):

    def __init__(self, start):
        self.value = start
        self.next = []


nodes = {}
visited = set()
end_nodes = set()
for p in pairs:
    start, end = p.split()

    # build a node for start point
    if start not in visited:
        start_node = Node(start)
        nodes[start] = start_node
    # build a node for end point
    if end not in visited:
        end_node = Node(end)
        nodes[end] = end_node
    # build a link for these two links
    visited.add(start)
    visited.add(end)
    end_nodes.add(end)
    nodes[start].next.append(nodes[end])

heads = sorted(visited.difference(end_nodes))

for head in heads:
    end_points = set()
    dfs(nodes[head], end_points)
    end_points = sorted(end_points)
    print(f"{head} : {' '.join(end_points)}")
