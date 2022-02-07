'''LinkedList implementation'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, first_node: Node):
        self.first_node = first_node

    def read(self, index):
        # Start at the first node in the list.
        current_node = self.first_node
        current_index = 0
        while current_index < index:
            current_node = current_node.next
            current_index += 1
            # Check if we've reached the end of the list.
            if current_node is None:
                return None
        return current_node

    def insert_at_index(self, value, index):
        """Insert a new value at a certain index."""
        # First create the new node.
        new_node = Node(value)
        # check if we're inserting at the beginning of the list.
        if index == 0:
            # Link the new node to the (previous)first node.
            new_node.next = self.first_node
            # Make the new node the first node.
            self.first_node = new_node
            return
        # If we are not inserting at the beginning.
        current_node = self.first_node
        current_index = 0
        # Get the node immediately before the new node will go.
        while current_index < index - 1:
            current_node = current_node.next
            current_index += 1
            if current_node is None:
                return
        # Link the new node to the next node.
        new_node.next = current_node.next
        # Link the previous node to the new node.
        current_node.next = new_node

    def index_of(self, value):
        """Search for a value and return its index."""
        current_node = self.first_node
        current_index = 0
        while current_node is not None:
            if current_node.value == value:
                return current_index
            current_node = current_node.next
            current_index += 1
        # The item is not in the list.
        return None

    def delete_at_index(self, index):
        """Delete the item at the given index."""
        if index == 0:
            self.first_node = self.first_node.next
            return
        current_node = self.first_node
        current_index = 0
        while current_index < index - 1:
            current_node = current_node.next
            current_index += 1
            if current_node is None:
                return
        # Link the current node to the one after the one we want to delete.
        current_node.next = current_node.next.next


def count_element(linked_list: LinkedList, value):
    """Count the number of occurrences of an element in a linked list."""
    # Base case
    if linked_list.first_node.next is None:
        if linked_list.first_node.value == value:
            return 1
        else:
            return 0
    if linked_list.first_node.value == value:
        return 1 + count_element(LinkedList(linked_list.first_node.next), value)
    else:
        return 0 + count_element(LinkedList(linked_list.first_node.next), value)


if __name__ == '__main__':
    node_1 = Node('1')
    node_2 = Node('2')
    node_3 = Node('3')
    node_4 = Node('4')

    linked_list = LinkedList(node_1)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    # Insert a new element.
    linked_list.insert_at_index('5', 2)
    print(linked_list.read(2).value)
    # Delete an element.
    print()
    linked_list.delete_at_index(2)
    print(linked_list.read(2).value)
    # Count the number of occurrences of an element.
    print()
    linked_list.insert_at_index('3', 2)
    linked_list.insert_at_index('3', 2)
    linked_list.insert_at_index('3', 2)
    print(count_element(linked_list, '3'))
