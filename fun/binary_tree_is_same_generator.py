# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q) -> bool:
        
    def tree_generator(root):
        def inorder(node):
            if node:
                yield node.val
                yield from inorder(node.left)
                yield from inorder(node.right)

            else:
                yield None

        if not root:
            return

        yield from inorder(root)
    
    p_gen = tree_generator(p)
    q_gen = tree_generator(q)
    
    while (item := next(p_gen, -1)) != -1:
        item2 = next(q_gen, -1)
        print(item, item2)
        if item != item2:
            return False
    
    if next(p_gen, -1) != next(q_gen, -1):
        return False
    
    return True

# Example usage:
# Creating two binary trees
tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
tree2 = TreeNode(1, None, TreeNode(2))

# Checking if the trees are the same
result = isSameTree(tree1, tree2)

print("Are the trees the same?", result)