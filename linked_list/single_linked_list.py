class Node:
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
    def __init__(self):
        self._length = 0
        self.head = Node()

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, head_node):
        self._head = head_node

    def insert_at_beginning(self, data):
        new_node = Node()
        new_node.data = data
        if self._length == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._length += 1

    def insert_at_end(self, data):
        new_node = Node()
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
        if pos > self._length or pos < 0:
            raise Exception

        if pos == 0:
            self.insert_at_beginning(data)
        else:
            new_node = Node()
            new_node.data = data
            current_node = self.head
            for i in range(pos-1):
                current_node = current_node.next

            new_node.next = current_node.next
            current_node.next = new_node

            self._length += 1

    def __add__(self, data):
        self.insert_at_end(data)
        return self

    def delete_from_beginning(self):
        if self._length == 0:
            raise Exception

        self.head = self.head.next
        if not self.head:
            self.head = Node()

        self._length -= 1

    def delete_from_end(self):
        if self._length == 0:
            raise Exception

        if self._length == 1:
            self.head = Node()
        else:
            current_node = self.head

            for _ in range(self._length-1):
                current_node = current_node.next

            current_node.next = None
        self._length -= 1

    def delete(self, pos=0):
        if pos >= self._length or pos < 0:
            raise Exception

        if pos == 0:
            self.delete_from_beginning()
        elif pos == self._length-1:
            self.delete_from_end()
        else:
            current_node = self.head
            for i in range(pos-1):
                current_node = current_node.next

            current_node.next=current_node.next.next
            self._length -= 1

    def traverse_list(self):
        node = self._head
        print(f'{node.data}', end='')

        for each_node in range(1, self._length):
            node = node.next
            if not node:
                break
            print(f'--->{node.data}', end='')

        print('')

    def __len__(self):
        return self._length
