class NodeList:
    """Node of sorted linked list"""

    def __init__(self, key, data=None, next=None):
        self.key = key
        self.data = data
        self.next = next


class LinkedList:
    """Sorted linked list

    >>> mylist = LinkedList()
    >>> mylist[5] = 'I am node with key 5'
    >>> mylist[8] = 'I am node with key 8'
    >>> mylist[10] = 'I am node with key 10'
    >>> mylist[7] = 'I am node with key 7'
    >>> mylist[9] = 'I am node with key 9'
    >>> mylist[3] = 'I am node with key 3'
    >>> mylist.first.key
    3
    >>> len(mylist)
    6
    >>> mylist[7]
    'I am node with key 7'
    >>> mylist[3]
    'I am node with key 3'
    >>> mylist[10]
    'I am node with key 10'
    >>> mylist[7] = 'Now I am node with key seven'
    >>> mylist[7]
    'Now I am node with key seven'
    >>> del mylist[3]
    >>> del mylist[7]
    >>> del mylist[10]
    >>> len(mylist)
    3
    """

    def __init__(self):
        self.first = None
        self._size = 0  # number of node in the list

    def __len__(self):
        return self._size

    def __contains__(self, key):  # key in self
        try:
            self._get(key, self.first)
        except KeyError:
            return False
        return True

    def keys(self):
        current_node = self.first
        while current_node:
            yield current_node.key
            current_node = current_node.next

    def values(self):
        current_node = self.first
        while current_node:
            yield current_node.data
            current_node = current_node.next

    def items(self):
        current_node = self.first
        while current_node:
            yield current_node.key, current_node.data
            current_node = current_node.next

    def __iter__(self):
        return self.keys()

    def __setitem__(self, key, data):
        """Method add new node in the linked list or change data in existing node"""
        if not self.first or key < self.first.key:
            self.first = NodeList(key, data, self.first)
            self._size += 1
        else:  # key > self.first.key
            self._put(key, data, self.first)

    def _put(self, key, data, current_node):
        """Auxiliary method for __setitem__"""
        if key == current_node.key:
            current_node.data = data
        else:  # key > current_node.key
            if not current_node.next or key < current_node.next.key:
                current_node.next = NodeList(key, data, current_node.next)
                self._size += 1
            else:  # key >= current_node.next.key
                self._put(key, data, current_node.next)

    def __getitem__(self, key):
        """Method finds node in linked list by key and gives node's data
        or raises exception KeyError
        """
        return self._get(key, self.first).data

    def _get(self, key, current_node):
        """Auxiliary method for __getitem__"""
        if not current_node or key < current_node.key:
            raise KeyError('Key {} is not found in the linked list'.format(key))
        elif key == current_node.key:
            return current_node
        else:  # key >= current_node.key
            return self._get(key, current_node.next)

    def __delitem__(self, key):
        """Method deletes node in linked list or raises exception KeyError"""
        self._del(key, None, self.first)

    def _del(self, key, previous_node, current_node):
        """Auxiliary method for __delitem__"""
        if not current_node or key < current_node.key:
            raise KeyError('Key {} is not found in the linked list'.format(key))
        elif key == current_node.key:
            if not previous_node:
                self.first = current_node.next
            else:
                previous_node.next = current_node.next
            self._size -= 1
        else:  # key >= current_node.key
            self._del(key, current_node, current_node.next)

    def __add__(self, other):
        result = LinkedList()
        current_self = self.first
        current_other = other.first
        while True:
            if current_self and current_other:
                if current_self.key <= current_other.key:
                    result[current_self.key] = current_self.data
                    current_self = current_self.next
                else:
                    result[current_other.key] = current_other.data
                    current_other = current_other.next
            elif current_self and not current_other:
                result[current_self.key] = current_self.data
                current_self = current_self.next
            elif not current_self and current_other:
                result[current_other.key] = current_other.data
                current_other = current_other.next
            else:
                return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()