import streamlit as st

class Node:
    def __init__(self, data, name, room_id):
        self.prev = None
        self.data = data
        self.name = name
        self.room_id = room_id
        self.next = None

class HotelManagementApp:
    def __init__(self):
        self.head = None
        self.tail = None

    def room_allocation(self, cnic, name, room_id):
        if self.head is None:
            self.head = Node(cnic, name, room_id)
            self.tail = self.head
        else:
            new_node = Node(cnic, name, room_id)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display_rooms(self):
        current_node = self.head
        display_text = ""
        while current_node:
            display_text += f"{current_node.data} {current_node.name} {current_node.room_id}\n"
            current_node = current_node.next
        return display_text

    def backward_display(self):
        current_node = self.tail
        display_text = ""
        while current_node:
            display_text += f"{current_node.data} {current_node.name} {current_node.room_id}\n"
            current_node = current_node.prev
        return display_text

    def de_allocation(self, num):
        current_node = self.head

        if current_node.data == num:
            self.head = current_node.next
            if self.head:
                self.head.prev = None
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

app = HotelManagementApp()

# Streamlit UI
st.title("Hotel Management System")

menu_options = ["Room Allotment", "All Room Display (Oldest to Newest)", "Display Room (Newest to Oldest)", "Delete Room Allocation"]
selected_menu = st.sidebar.selectbox("Select Option", menu_options)

if selected_menu == "Room Allotment":
    cnic = st.text_input("CNIC Number:")
    name = st.text_input("Name:")
    room_id = st.text_input("Room ID:")
    if st.button("Allocate Room"):
        app.room_allocation(cnic, name, room_id)
        st.success("Room Allocated Successfully!")

elif selected_menu == "All Room Display (Oldest to Newest)":
    st.text(app.display_rooms())

elif selected_menu == "Display Room (Newest to Oldest)":
    st.text(app.backward_display())

elif selected_menu == "Delete Room Allocation":
    delete_cnic = st.text_input("CNIC Number:")
    if st.button("Delete Allocation"):
        app.de_allocation(delete_cnic)
        st.success(f"Room Allocation for CNIC {delete_cnic} Deleted Successfully!")

# Note: This Streamlit app is a simplified example and may need further adjustments based on your requirements.
