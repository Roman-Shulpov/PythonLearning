class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index):
        if self.head is None:
            return None
        i = 0
        node = self.head
        while i != index:
            i += 1
            node = node.next
            if node is None:
                return None
        return node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, index):
        prev_node = self.get(index - 1)
        current_node = self.get(index)
        if prev_node is None or current_node is None:
            return
        prev_node.next = current_node.next

    def get_all(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


# Пример использования
sll = SingleLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(6)
sll.append(3)
sll.get(13)
sll.remove(5)

node_3 = sll.get(3)
node_3_value = node_3.data
print(node_3_value)

print("Элементы списка:", sll.get_all())
print("Длина списка:", sll.length())
