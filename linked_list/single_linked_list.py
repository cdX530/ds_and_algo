"""
Implementation of a Single Linked List
"""


class _Node:
    """
    Represents each node in the Linked List
    """
    def __init__(self):
        self._data = None
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_node):
        self._next = next_node

    def has_next(self):
        return self.next is not None


class SingleLinkedList:
    """
    Implementation of a Single Linked List
    """
    def __init__(self):
        self._length = 0
        self.head = _Node()

    @property
    def head(self):
        """
        Getter for getting the head of the list
        :return:
        """
        return self._head

    @head.setter
    def head(self, head_node):
        """
        Setter to set the head node
        :param head_node:
        :return:
        """
        self._head = head_node

    def insert_at_beginning(self, data):
        """
        Inserts the data into a new node at the beginning of the list
        :param data: data to be inserted
        """
        new_node = _Node()
        new_node.data = data
        if self._length == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._length += 1

    def insert_at_end(self, data):
        """
        Inserts the data into a new node at the end of the list
        :param data: data to be inserted
        """
        new_node = _Node()
        new_node.data = data

        if self._length == 0:
            self.head = new_node
        else:
            traversal_node = self.head
            while traversal_node.next:
                traversal_node = traversal_node.next

            traversal_node.next = new_node

        self._length += 1

    def insert(self, data, pos=0):
        """
        Inserts data into a new node at the specified position in the list
        :param data: data to be inserted
        :param pos: position at which the data is to be inserted in the list.
                    Defaults to 0.
        """
        if pos > self._length or pos < 0:
            print("Cannot insert on positions greater than length")

        if pos == 0:
            self.insert_at_beginning(data)
        else:
            new_node = _Node()
            new_node.data = data
            current_node = self.head
            for i in range(pos-1):
                current_node = current_node.next

            new_node.next = current_node.next
            current_node.next = new_node

            self._length += 1

    def delete_from_beginning(self):
        """
        Deletes the node from the beginning of the list
        """
        if self._length == 0:
            print("Cannot delete from empty list")

        self.head = self.head.next
        if not self.head:
            self.head = _Node()

        self._length -= 1

    def delete_from_end(self):
        """
        Deletes the node from the end of the list
        """
        if self._length == 0:
            print("Cannot delete from empty list")

        if self._length == 1:
            self.head = _Node()
        else:
            current_node = self.head

            for _ in range(self._length-1):
                current_node = current_node.next

            current_node.next = None
        self._length -= 1

    def delete(self, pos=0):
        """
        Deletes the node from the specified position in the list
        :param pos: position of the node to be deleted
        """
        if pos >= self._length or pos < 0:
            print("Position should be whole number less than length of list")

        if pos == 0:
            self.delete_from_beginning()
        elif pos == self._length-1:
            self.delete_from_end()
        else:
            current_node = self.head
            for i in range(pos-1):
                current_node = current_node.next

            current_node.next = current_node.next.next
            self._length -= 1

    def print_list(self):
        """
        Prints the list.
        """
        node = self._head
        print(f'{node.data}', end='')

        for each_node in range(1, self._length):
            node = node.next
            if not node:
                break
            print(f'--->{node.data}', end='')

        print('')

    def __len__(self):
        """
        Gives the length of the list
        """
        return self._length

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
