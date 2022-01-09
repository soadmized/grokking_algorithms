class Node:

    def __init__(self, data, next=None):
        self.next = next
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


class LinkedList:

    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, data):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root += 1
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def find(self, data):
        this_node = self.root
        while this_node:
            if this_node.get_data() == data:
                return data
            else:
                this_node = this_node.get_next()
        return None


if __name__ == '__main__':

    linked_list = LinkedList()
    linked_list.add(5)
    linked_list.add(5)
    linked_list.add(8)
    print(linked_list.find(5))
