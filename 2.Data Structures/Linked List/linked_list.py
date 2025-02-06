# Node class represents a single node in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Store the data in the node
        self.next = None  # Next node reference (initially None)


# LinkedList class represents the linked list itself
class LinkedList:
    def __init__(self):
        self.head = None  # The linked list starts with no nodes

    # Method to append data to the linked list
    def append(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:
            # If the list is empty, the new node becomes the head
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next  # Traverse the list until the last node
        last.next = new_node  # Link the last node to the new node

    # Method to print the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Method to search for a value in the linked list
    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True  # Value found
            current = current.next
        return False  # Value not found

    # Method to delete a node with a specific value
    def delete(self, value):
        current = self.head

        # If the node to be deleted is the head node
        if current and current.data == value:
            self.head = current.next  # Move the head to the next node
            return

        prev = None
        while current:
            if current.data == value:
                break
            prev = current
            current = current.next

        # If the value was not found
        if current is None:
            print(f"Value {value} not found in the list.")
            return

        # Unlink the node from the linked list
        prev.next = current.next
        current = None  # Free the memory (optional in Python)


# Main method to test the LinkedList class
def main():
    ll = LinkedList()

    # Append data to the linked list
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)

    # Print the list
    print("Linked List:")
    ll.print_list()  # Output: 10 -> 20 -> 30 -> 40 -> None

    # Search for a value
    print("\nSearch for value 20:")
    print(ll.search(20))  # Output: True

    print("\nSearch for value 50:")
    print(ll.search(50))  # Output: False

    # Delete a value
    print("\nDelete value 30:")
    ll.delete(30)

    # Print the list after deletion
    ll.print_list()  # Output: 10 -> 20 -> 40 -> None

    # Try deleting a value that doesn't exist
    print("\nDelete value 50 (not in list):")
    ll.delete(50)  # Output: Value 50 not found in the list.


# Run the main method
if __name__ == "__main__":
    main()
