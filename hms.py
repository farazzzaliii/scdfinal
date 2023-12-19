class Node:
    def __init__(self, data, name, room_id):
        self.prev = None
        self.data = data
        self.name = name
        self.room_id = room_id
        self.next = None


head = None
tail = None


def room_allocation():
    global head, tail
    cnic = int(input("Enter the CNIC number of the customer: "))
    name = input("Enter the name of the customer: ")
    room_id = input("Enter the room id: ")

    if head is None:
        head = Node(cnic, name, room_id)
        tail = head
    else:
        new_node = Node(cnic, name, room_id)
        new_node.prev = tail
        tail.next = new_node
        tail = new_node


def display_rooms():
    current_node = head
    while current_node:
        print(current_node.data, current_node.name, current_node.room_id)
        current_node = current_node.next
    print()


def backward_display():
    current_node = tail
    while current_node:
        print(current_node.data, current_node.name, current_node.room_id)
        current_node = current_node.prev
    print()


def de_allocation():
    num = int(input("Enter the CNIC number of the customer: "))
    global head, tail

    current_node = head

    if current_node.data == num:
        head = current_node.next
        if head:
            head.prev = None
        del current_node
        return

    while current_node:
        if current_node.data == num:
            prev_node = current_node.prev
            next_node = current_node.next
            prev_node.next = next_node
            if next_node:
                next_node.prev = prev_node
            del current_node
            return
        current_node = current_node.next

    print(f"Element {num} not Found.")
2

def menu():
    while True:
        print("\n\t\t\tWELCOME TO HOTEL XYZ \t\t")
        print("\t\t1: Room allotment \t\t")
        print("\t\t2: All room display (oldest to newest) \t\t")
        print("\t\t3: Display room (Newest to oldest) \t\t")
        print("\t\t4: Delete room allocation \t\t")

        choice = int(input("Choose any number: "))

        if choice == 1:
            room_allocation()
        elif choice == 2:
            display_rooms()
        elif choice == 3:
            backward_display()
        elif choice == 4:
            de_allocation()
        else:
            print("Invalid input.")
            break


if __name__ == "__main__":
    menu()
