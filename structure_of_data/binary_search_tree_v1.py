class Tree:
    """Binary search tree

    >>> mytree = Tree()
    >>> mytree[5] = 'I am node with key 5'
    >>> mytree[3] = 'I am node with key 3'
    >>> mytree[12] = 'I am node with key 12'
    >>> mytree[1] = 'I am node with key 1'
    >>> mytree[6] = 'I am node with key 6'
    >>> mytree[14] = 'I am node with key 14'
    >>> mytree[4] = 'I am node with key 4'
    >>> mytree[8] = 'I am node with key 8'
    >>> mytree[10] = 'I am node with key 10'
    >>> mytree[7] = 'I am node with key 7'
    >>> mytree[9] = 'I am node with key 9'
    >>> mytree[16] = 'I am node with key 16'
    >>> len(mytree)
    12
    >>> mytree[5]
    'I am node with key 5'
    >>> mytree[12]
    'I am node with key 12'
    >>> mytree[10]
    'I am node with key 10'
    >>> 16 in mytree
    True
    >>> 24 in mytree
    False
    >>> del mytree[5]
    >>> del mytree[12]
    >>> del mytree[3]
    >>> del mytree[4]
    >>> del mytree[1]
    >>> len(mytree)
    7
    >>> del mytree[6]
    >>> del mytree[14]
    >>> del mytree[16]
    >>> del mytree[10]
    >>> del mytree[7]
    >>> del mytree[9]
    >>> len(mytree)
    1
    >>> del mytree[8]
    """

    def __init__(self):
        self.root = None
        self._size = 0  # number of elements in the tree

    def __len__(self):  # number of elements in the tree
        return self._size

    def __setitem__(self, key, data):
        """Method adds new node in the tree or change data in existing node"""
        if self.root:
            self._put(key, data, self.root)
        else:
            self.root = TreeNode(key, data)
            self._size += 1

    def _put(self, key, data, current_node):
        if key == current_node.key:
            current_node.data = data
        elif key > current_node.key:
            if current_node.hasRightChild():
                self._put(key, data, current_node.rightChild)
            else:
                current_node.rightChild = TreeNode(key, data, parent=current_node)
                self._size += 1
        else:
            if current_node.hasLeftChild():
                self._put(key, data, current_node.leftChild)
            else:
                current_node.leftChild = TreeNode(key, data, parent=current_node)
                self._size += 1

    def __getitem__(self, key):
        """Method finds node in tree by key and gives node's data
         or raises exception KeyError
         """
        if self.root:
            return self._get(key, self.root).data
        else:
            raise KeyError('Key {} is not found in the tree'.format(key))

    def _get(self, key, current_node):
        """Function finds node in tree by key or raises exception KeyError"""
        if not current_node:
            raise KeyError('Key {} is not found in the tree'.format(key))
        elif key == current_node.key:
            return current_node
        elif key > current_node.key:
            return self._get(key, current_node.rightChild)
        else:
            return self._get(key, current_node.leftChild)

    def __contains__(self, key):
        try:
            self._get(key, self.root)
        except KeyError:
            return False
        return True

    def __delitem__(self, key):
        """Method deletes node in tree or raises exception KeyError"""
        del_node = self._get(key, self.root)
        if del_node.isLeaf():
            self._del_leaf(del_node)
        elif del_node.hasBothChildren():
            self._del_node_has_both_children(del_node)
        else:  # del_node has only one child
            self._del_node_has_one_child(del_node)
        self._size -= 1

    def _del_leaf(self, del_node):
        if del_node.isRoot():
            self.root = None
        elif del_node.isRightChild():
            del_node.parent.rightChild = None
        else:  # del_node.isLeftChild()
            del_node.parent.leftChild = None

    def _del_node_has_one_child(self, del_node):
        if del_node.hasRightChild():
            replacement = del_node.rightChild
        else:  # del_node.hasLeftChild()
            replacement = del_node.leftChild
        if del_node.isRoot():
            replacement.parent = None
            self.root = replacement
        elif del_node.isRightChild():
            del_node.parent.rightChild = replacement
            replacement.parent = del_node.parent
        else:  # del_node.isLeftChild()
            del_node.parent.leftChild = replacement
            replacement.parent = del_node.parent

    def _del_node_has_both_children(self, del_node):
        replacement = self._most_left(del_node.rightChild)
        if replacement.isLeaf():
            self._del_leaf(replacement)
        else:  # replacement has only one child
            self._del_node_has_one_child(replacement)
        if del_node.isRoot():
            self.root = replacement
            replacement.parent = None
        elif del_node.isRightChild():
            del_node.parent.rightChild = replacement
            replacement.parent = del_node.parent
        else:  # del_node.isLeftChild()
            del_node.parent.leftChild = replacement
            replacement.parent = del_node.parent
        del_node.rightChild.parent = replacement
        del_node.leftChild.parent = replacement
        replacement.rightChild = del_node.rightChild
        replacement.leftChild = del_node.leftChild

    def _most_left(self, current_node):
        if current_node.hasLeftChild():
            return self._most_left(current_node.leftChild)
        else:
            return current_node

    def _most_right(self, current_node):
        if current_node.hasRightChild():
            return self._most_right(current_node.rightChild)
        else:
            return current_node


class TreeNode:
    """Node of binary search tree"""

    def __init__(self, key, data, left=None, right=None, parent=None):
        self.key = key  # must be int or str
        self.data = data
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        if self.leftChild:
            return True
        else:
            return False

    def hasRightChild(self):
        if self.rightChild:
            return True
        else:
            return False

    def hasAnyChildren(self):
        if self.leftChild or self.rightChild:
            return True
        else:
            return False

    def hasBothChildren(self):
        if self.leftChild and self.rightChild:
            return True
        else:
            return False

    def isLeftChild(self):
        return self.parent and (self.parent.leftChild == self)  # True or False

    def isRightChild(self):
        return self.parent and (self.parent.rightChild == self)  # True or False

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        if self.leftChild or self.rightChild:
            return False
        else:
            return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
