class T:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def LCA(root, x, y):
    if root == None:
        return None
    elif root.val == x or root.val == y:
        return root
    else:
        left = LCA(root.left, x, y)
        right = LCA(root.right, x, y)
        if left == None: return right
        if right == None: return left
        return root

#tree = T(3, T(1, T(0, None, None), T(2, None, None)), T(5, T(4, None, None), T(8, T(7, T(6, None, None), None), T(9, None, None))))
#print(LCA(tree, 2, 6).val)
