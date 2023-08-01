"""
# 589. N-ary Tree Preorder Traversal
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack_arr = []
        output_arr = []

        if not root:
            return output_arr

        stack_arr.append(root)
        while (len(stack_arr) > 0):
            node = stack_arr.pop(0)
            output_arr.append(node.val)
            node.children.reverse()
            for n in node.children:
                stack_arr.insert(0, n)
        return output_arr
