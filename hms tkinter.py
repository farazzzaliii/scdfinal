import streamlit as streamlit
import tkinter as tk
from tkinter import ttk

class Node:
    def __init__(self, data, name, room_id):
        self.prev = None
        self.data = data
        self.name = name
        self.room_id = room_id
        self.next = None

class HotelManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")

        self.head = None
        self.tail = None

        self.create_widgets()

    def create_widgets(self):
        # GUI components
        self.label = ttk.Label(self.root, text="WELCOME TO HOTEL XYZ")
        self.label.grid(row=0, column=0, columnspan=4, pady=10)

        self.notebook = ttk.Notebook(self.root)
        self.notebook.grid(row=1, column=0, columnspan=4, pady=10)

        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Room Allotment")

        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="All Room Display (Oldest to Newest)")

        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab3, text="Display Room (Newest to Oldest)")

        self.tab4 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab4, text="Delete Room Allocation")

        # Tab 1 - Room Allotment
        ttk.Label(self.tab1, text="CNIC Number:").grid(row=0, column=0)
        self.cnic_entry = ttk.Entry(self.tab1)
        self.cnic_entry.grid(row=0, column=1)

        ttk.Label(self.tab1, text="Name:").grid(row=1, column=0)
        self.name_entry = ttk.Entry(self.tab1)
        self.name_entry.grid(row=1, column=1)

        ttk.Label(self.tab1, text="Room ID:").grid(row=2, column=0)
        self.room_id_entry = ttk.Entry(self.tab1)
        self.room_id_entry.grid(row=2, column=1)

        ttk.Button(self.tab1, text="Allocate Room", command=self.room_allocation).grid(row=3, column=0, columnspan=2, pady=10)

        # Tab 2 - All Room Display
        self.display_text1 = tk.Text(self.tab2, height=10, width=40)
        self.display_text1.grid(row=0, column=0, pady=10)

        # Tab 3 - Display Room
        self.display_text2 = tk.Text(self.tab3, height=10, width=40)
        self.display_text2.grid(row=0, column=0, pady=10)

        # Tab 4 - Delete Room Allocation
        ttk.Label(self.tab4, text="CNIC Number:").grid(row=0, column=0)
        self.delete_cnic_entry = ttk.Entry(self.tab4)
        self.delete_cnic_entry.grid(row=0, column=1)

        ttk.Button(self.tab4, text="Delete Allocation", command=self.de_allocation).grid(row=1, column=0, columnspan=2, pady=10)

    def room_allocation(self):
        cnic = int(self.cnic_entry.get())
        name = self.name_entry.get()
        room_id = self.room_id_entry.get()

        if self.head is None:
            self.head = Node(cnic, name, room_id)
            self.tail = self.head
        else:
            new_node = Node(cnic, name, room_id)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        # Update the displayed information in tabs 2 and 3
        self.update_display_tabs()

    def update_display_tabs(self):
        # Clear previous content
        self.display_text1.delete(1.0, tk.END)
        self.display_text2.delete(1.0, tk.END)

        # Update All Room Display (tab 2)
        current_node = self.head
        while current_node:
            self.display_text1.insert(tk.END, f"{current_node.data} {current_node.name} {current_node.room_id}\n")
            current_node = current_node.next

        # Update Display Room (tab 3)
        current_node = self.tail
        while current_node:
            self.display_text2.insert(tk.END, f"{current_node.data} {current_node.name} {current_node.room_id}\n")
            current_node = current_node.prev

    def backward_display(self):
        current_node = self.tail
        display_text = ""
        while current_node:
            display_text += f"{current_node.data} {current_node.name} {current_node.room_id}\n"
            current_node = current_node.prev
        return display_text

    def de_allocation(self):
        num = int(self.delete_cnic_entry.get())
        current_node = self.head

        if current_node.data == num:
            self.head = current_node.next
            if self.head:
                self.head.prev = None
            del current_node
            self.update_display_tabs()
            return

        while current_node:
            if current_node.data == num:
                prev_node = current_node.prev
                next_node = current_node.next
                prev_node.next = next_node
                if next_node:
                    next_node.prev = prev_node
                del current_node
                self.update_display_tabs()
                return
            current_node = current_node.next

        print(f"Element {num} not Found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementApp(root)
    root.mainloop()
