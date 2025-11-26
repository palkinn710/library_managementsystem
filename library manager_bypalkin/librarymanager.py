# Library Management System
# Name       : Palkin Jain
# Course     : Programming for Problem Solving using Python
# Roll No.   : 2501410045

class LibraryManager:
    def __init__(self, db_file="library.txt"):
        self.db_file = db_file

        # Create the file if missing
        try:
            open(self.db_file, "r").close()
        except FileNotFoundError:
            open(self.db_file, "w").close()

    def insert_book(self, name, writer, code):
        with open(self.db_file, "a") as file:
            file.write(f"{name},{writer},{code},available\n")
        print("Book added to collection.")

    def checkout_book(self, code):
        with open(self.db_file, "r") as file:
            entries = file.readlines()

        updated = []
        hit = False

        for row in entries:
            parts = row.strip().split(",")

            if parts[2] == code:
                hit = True
                if parts[3] == "available":
                    parts[3] = "issued"
                    print("Book issued to user.")
                else:
                    print("Book is not available right now.")
            updated.append(",".join(parts) + "\n")

        if not hit:
            print("No book found with that ISBN.")
            return

        with open(self.db_file, "w") as file:
            file.writelines(updated)

    def receive_book(self, code):
        with open(self.db_file, "r") as file:
            all_data = file.readlines()

        newset = []
        match = False

        for row in all_data:
            parts = row.strip().split(",")

            if parts[2] == code:
                match = True
                if parts[3] == "issued":
                    parts[3] = "available"
                    print("Book returned successfully.")
                else:
                    print("This book was already available.")
            newset.append(",".join(parts) + "\n")

        if not match:
            print("ISBN not found in records.")
            return

        with open(self.db_file, "w") as file:
            file.writelines(newset)

    def find_title(self, keyword):
        with open(self.db_file, "r") as file:
            records = file.readlines()

        status = False

        for line in records:
            fields = line.strip().split(",")
            if keyword.lower() in fields[0].lower():
                print(f"Title: {fields[0]}  Author: {fields[1]}  ISBN: {fields[2]}  Status: {fields[3]}")
                status = True

        if not status:
            print("No books found with similar title.")

    def list_all(self):
        with open(self.db_file, "r") as file:
            records = file.readlines()

        if not records:
            print("Library is currently empty.")
            return

        for line in records:
            fields = line.strip().split(",")
            print(f"Title: {fields[0]}, Author: {fields[1]}, ISBN: {fields[2]}, Status: {fields[3]}")


# ---------------- UI Section ---------------- #

lib_app = LibraryManager()

while True:
    print("\n====== Library Control Panel ======")
    print("1. Add New Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Complete Inventory")
    print("5. Search Book by Title")
    print("6. Quit")

    option = input("Choose an option: ")

    if option == "1":
        n = input("Book title: ")
        w = input("Author name: ")
        c = input("ISBN code: ")
        lib_app.insert_book(n, w, c)

    elif option == "2":
        c = input("Enter ISBN to issue: ")
        lib_app.checkout_book(c)

    elif option == "3":
        c = input("Enter ISBN to return: ")
        lib_app.receive_book(c)

    elif option == "4":
        lib_app.list_all()

    elif option == "5":
        t = input("Enter title keyword: ")
        lib_app.find_title(t)

    elif option == "6":
        print("Closing system...")
        break

    else:
        print("Invalid option. Try again.")
