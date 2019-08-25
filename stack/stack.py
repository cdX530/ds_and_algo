from linked_list.single_linked_list import SingleLinkedList


class Stack:
    def __init__(self, length):
        self._list = SingleLinkedList()
        self.upper_limit = length

    def pop(self):
        if self.is_empty():
            print('StackUnderFlow')
        else:
            return self._list.delete_from_beginning()

    def push(self, n):
        if len(self._list) == self.upper_limit:
            print('StackOverFlow')
        else:
            self._list.insert_at_beginning(n)

    def peek(self):
        return self._list.head.data

    def is_empty(self):
        if len(self._list) == 0:
            return True
        else:
            return False
