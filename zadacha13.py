#възел в свързания списък със стойност и указател към следващия възел
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DynamicCircularLinkedList:

    def __init__(self):
        #указател към първия възел
        self.head = None
        #указател към последния възел
        self.tail = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

        if self.size >= 2 ** (self.size.bit_length() - 1):
            self.double_size()

    def double_size(self):
        current = self.head
        for _ in range(self.size - 1):
            current = current.next

        self.tail.next = current.next
        self.tail = current

    def delete(self, value):
        if not self.head:
            print("List is empty")
            return

        current = self.head
        prev = None
        found = False

        while current and not found:
            if current.data == value:
                found = True
            else:
                prev = current
                current = current.next

        if found:
            if prev:
                prev.next = current.next
                if current == self.tail:
                    self.tail = prev
            else:
                self.head = current.next
                if current == self.tail:
                    self.tail = None


            self.size -= 1
            print(f"{value} is deleted")
        else:
            print(f"{value} is not in the list")

    def display(self):
        current = self.head
        if not current:
            print("List is empty")
        else:
            while current:
                print(current.data, end=";")
                current = current.next
                if current == self.head:
                    break
            print()


if __name__ == "__main__":
    list = DynamicCircularLinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    list.display()
    list.append(4)
    list.display()
    list.delete(3)
    list.display()
    list.append(5)
    list.display()
