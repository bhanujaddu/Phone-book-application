import tkinter as tk
from tkinter import messagebox

class Phone:
    def __init__(self, PhoneData=None, next=None):
        self.data = PhoneData
        self.next = next

class PhoneBook:
    def __init__(self):
        self.head = None

    def search_Phone_Data(self, Phone_Data):
        if self.head is None:
            return None
        n = self.head
        while n is not None:
            if n.data == Phone_Data:
                return True
            n = n.next
        return False

    def Update_Phone_Data(self, old_Phone_Data, New_Phone_Data):
        if self.head is None:
            return False
        if old_Phone_Data == New_Phone_Data:
            return False
        replace = self.head
        while replace is not None:
            if replace.data == old_Phone_Data:
                replace.data = New_Phone_Data
                return True
            replace = replace.next
        return False

    def Phone_Data_Insert(self, Phone_Data):
        newData = Phone(Phone_Data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newData
        else:
            self.head = newData

    def Display_Phone_Book(self):
        current = self.head
        phone_book_data = []
        while current:
            phone_book_data.append(current.data)
            current = current.next
        return phone_book_data


class PhoneBookGUI:
    def __init__(self, root, phone_book):
        self.root = root
        self.phone_book = phone_book

        # Window Title
        self.root.title("Buga PhoneBook")
        self.root.geometry("500x500")

        # Labels and Entry Fields
        self.label_name = tk.Label(self.root, text="Enter Name:")
        self.label_name.pack(pady=10)
        self.entry_name = tk.Entry(self.root)
        self.entry_name.pack(pady=10)

        self.label_phone = tk.Label(self.root, text="Enter Phone Number:")
        self.label_phone.pack(pady=10)
        self.entry_phone = tk.Entry(self.root)
        self.entry_phone.pack(pady=10)

        self.label_email = tk.Label(self.root, text="Enter Email:")
        self.label_email.pack(pady=10)
        self.entry_email = tk.Entry(self.root)
        self.entry_email.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add to Phonebook", command=self.add_to_phonebook)
        self.add_button.pack(pady=10)

        self.update_button = tk.Button(self.root, text="Update Record", command=self.update_record)
        self.update_button.pack(pady=10)

        self.search_button = tk.Button(self.root, text="Search Record", command=self.search_record)
        self.search_button.pack(pady=10)

        self.display_button = tk.Button(self.root, text="Display Phonebook", command=self.display_phonebook)
        self.display_button.pack(pady=10)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack(pady=10)

    def add_to_phonebook(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()

        if name and phone and email:
            self.phone_book.Phone_Data_Insert(name)
            self.phone_book.Phone_Data_Insert(phone)
            self.phone_book.Phone_Data_Insert(email)
            messagebox.showinfo("Success", f"Added {name}, {phone}, {email} to the phonebook.")
        else:
            messagebox.showerror("Error", "Please fill out all fields.")

    def update_record(self):
        old_data = self.entry_name.get()  # Use name as identifier for simplicity
        new_data = self.entry_phone.get()  # Assuming we want to update phone for now

        if self.phone_book.Update_Phone_Data(old_data, new_data):
            messagebox.showinfo("Success", f"Updated {old_data} to {new_data}.")
        else:
            messagebox.showerror("Error", "Record not found or invalid update.")

    def search_record(self):
        search_term = self.entry_name.get()
        if self.phone_book.search_Phone_Data(search_term):
            messagebox.showinfo("Success", f"{search_term} found in the phonebook.")
        else:
            messagebox.showerror("Not Found", f"{search_term} not found in the phonebook.")

    def display_phonebook(self):
        phonebook_data = self.phone_book.Display_Phone_Book()
        display_str = "\n".join(phonebook_data) if phonebook_data else "Phonebook is empty."
        messagebox.showinfo("Phonebook", display_str)


if __name__ == "__main__":
    phone_book = PhoneBook()

    # Prepopulate with sample data
    phone_book.Phone_Data_Insert("Abrar ul Hassan")
    phone_book.Phone_Data_Insert("03032033694")
    phone_book.Phone_Data_Insert("Abrarulhassan@gmail.com")
    phone_book.Phone_Data_Insert("Khalid Hussain")
    phone_book.Phone_Data_Insert("03026798776")
    phone_book.Phone_Data_Insert("KhalidHussian@gmail.com")

    root = tk.Tk()
    app = PhoneBookGUI(root, phone_book)
    root.mainloop()

       
