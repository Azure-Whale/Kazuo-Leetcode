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
# Since we have the tree built from the hashmap, and method to get ancestors for given node using dfs
# I will add an atrribute to the ancestors when I am searchnig nit. the distance between the given node and current parent
# Pick the ancestors having longest length


tree_child = [[14,1],[14,2],[1,3],[3,7],[2,4],[4,8],[5,4],[5,10]]

def get_tree(relationships):

    tree = dict()
    target_child = []
    roots = []
    for pair in tree_child:
        parent, chd = pair
        tree[chd] = tree.setdefault(chd,[])
        tree[parent] = tree.setdefault(parent,[])
        tree[chd].append(parent)

    for chd,parents in tree.items():
        if len(parents) == 1:
            target_child.append(chd)
        if len(parents) == 0:
            roots.append(chd)

    return (tree,roots)

tree ,root = get_tree(tree_child)

def have_common_ancestor(tree,root,node):
    ans = []
    if node not in root and node not in tree.keys():
        return None
    
    ancestors_A = set()
    dfs(node, ancestors_A)
    max_level = max(ancestors_A)[0]
    for item in ancestors_A:
        level,node = item
        if level == max_level:
            ans.append(node)
    print(ans)
    return ans

        
def dfs(node,ancestors,level=0):
    level += 1
    parents = tree[node]
    if not parents:
        return 
    for node in parents:
        ancestors.add((level,node))
        dfs(node,ancestors,level)
    return 

have_common_ancestor(tree,root,7)