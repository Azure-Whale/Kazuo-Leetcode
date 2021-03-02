"""
3道题
1. 给出一堆[parent,child] 然后问 1个parent， 0parent的点
2. 同样的[parent,child] 返回两个点是否有common ancestor
3. 差不多的 pairs， 找出x earliest ancestor。

每题都要分析 复杂度，然后 所有测试都要跑一遍...
写了2题，然后第3题讲完思路

总体而言，挺舒服的一个面试。

随便画个 测试的图
         14
         / \
       1    2      5
      /       \   /    \
     3         4       10
       \       /
        7    8
"""
# find node with 0 parent and those with 1 parent
tree_child = [[14,1],[14,2],[1,3],[3,7],[2,4],[4,8],[5,4],[5,10]]
# Time Complexity O(E) ,E is the number of relationships, Because It is actually Graph problem and used an adjancency list but I didn't traverse it
#  Overall Space Complexity: O(E+V) Because It is actually Graph problem and used an adjancency list
# the Key is child, and value is a list of parents


def get_tree(relationships):
    # build graph, and build a dict to count parent(in-degree) for each node
    graph = dict()
    all_nodes = dict()
    for pair in tree_child:
        parent,child = pair
        graph[child] = graph.setdefault(child,[])
        graph[parent] = graph.setdefault(parent,[])
        graph[parent].append(child)
        all_nodes[parent] = all_nodes.setdefault(parent,0)
        all_nodes[child] = all_nodes.setdefault(child,0) + 1

    roots = []
    for node,indegree in all_nodes.items():
        if indegree == 0:
            roots.append(node)

    return (graph,roots)

tree ,root = get_tree(tree_child)

print(tree, root)





# tree = dict()
# target_child = []
# roots = []
# for pair in tree_child:
#     parent, chd = pair
#     tree[chd] = tree.setdefault(chd,[])
#     tree[parent] = tree.setdefault(parent,[])
#     tree[chd].append(parent)

# for chd,parents in tree.items():
#     if len(parents) == 1:
#         target_child.append(chd)
#     if len(parents) == 0:
#         roots.append(chd)
# print(roots)
# print(target_child)
