#възела в двоичното дърво
class TreeNode:
    def __init__(self, value):
        self.value = value
        #указател към ляво поддърво
        self.left = None
        #указател към дясно поддърво
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def print_values(self, start, traversal_type, condition):
        if traversal_type == "inorder":
            return self._inorder(start, [], condition)
        elif traversal_type == "preorder":
            return self._preorder(start, [], condition)
        elif traversal_type == "postorder":
            return self._postorder(start, [], condition)
        else:
            print("Invalid traversal type")
            return None

    #left-root-right
    def _inorder(self, start, result, condition):
        if start:
            result = self._inorder(start.left, result, condition)
            if condition(start.value):
                result.append(start.value)
            result = self._inorder(start.right, result, condition)
        return result

    #root-left-right
    def _preorder(self, start, result, condition):
        if start:
            if condition(start.value):
                result.append(start.value)
            result = self._preorder(start.left, result, condition)
            result = self._preorder(start.right, result, condition)
        return result

    #left-right-root
    def _postorder(self, start, result, condition):
        if start:
            result = self._postorder(start.left, result, condition)
            result = self._postorder(start.right, result, condition)
            if condition(start.value):
                result.append(start.value)
        return result


if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.root.left = TreeNode(-2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(-4)
    tree.root.right.left = TreeNode(-5)
    tree.root.right.right = TreeNode(6)

    positive_values = tree.print_values(tree.root, "inorder", lambda x: x > 0)
    print("Positive values(Inorder): ", positive_values)

    negative_values = tree.print_values(tree.root, "inorder", lambda x: x < 0)
    print("Negative values(Inorder): ", negative_values)


