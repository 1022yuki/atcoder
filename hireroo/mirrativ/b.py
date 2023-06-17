class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
#指定されたバイナリツリーの高さを計算する再帰的関数
def height(root):
    #ベースケース：空の木の高さは0です
    if root is None:
        return 0
    #は左右のサブツリーで繰り返され、最大深度を考慮します
    return 1 + max(height(root.left), height(root.right))

# from customtypes import TreeNode



# def solution(li):
#     # TODO: Implement me!
#     root = TreeNode(li[0])
#     lg = len(li)
#     Node = [None]*lg
#     for i in range(lg//2):
#         if li[2*i+1] != 'null':
#           Node[i].left = TreeNode(li[2*i+1])
#         if li[2*i+2] != 'null':
#           Node[i].right = TreeNode(li[2*i+2])
#     return height(root)

import math
def solution(root):
    # TODO: Implement me!
    lg = len(root)
    for i in range(lg-1, -1, -1):
        if root[i] != 'null':
            # print(root[i])
            return math.ceil(math.log2(root[i]+1))

# root = [1,2]
# root = [1]
# root = [1, None, None]
root = [1,2,3,'null',5,6,'null','null','null',10,11,'null','null','null','null']
# root = [1,2,3,4,5,6,7,8]
# root = [1,2,'null','null']

print(solution(root))