class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.issue_date = None

class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        print("\n---- Adding a Book ----")
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        try:
            isbn = int(input("Enter ISBN number: "))
        except ValueError:
            print("ISBN must be a number.")
            return
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully!")

    def issue_book(self):
        print("\n---- Issuing a Book ----")
        title = input("Enter title of book to issue: ")
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.issue_date is None:
                    issue_date = input("Enter issue date (DD-MM-YYYY): ")
                    book.issue_date = issue_date
                    print(f"Book '{book.title}' issued on {book.issue_date}")
                    return
                else:
                    print("This book is already issued.")
                    return
        print("Book not found.")

    def return_book(self):
        print("\n---- Returning a Book ----")
        title = input("Enter the title of book to return: ")
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.issue_date is not None:
                    book.issue_date = None
                    print(f"Book '{book.title}' returned successfully!")
                    return
                else:
                    print("This book was not issued.")
                    return
        print("Book not found.")

    def search_book(self):
        print("\n---- Searching for a Book ----")
        title = input("Enter the title of the book: ")
        for book in self.books:
            if book.title.lower() == title.lower():
                status = f"Issued on {book.issue_date}" if book.issue_date else "Available"
                print(f"\nTitle : {book.title}")
                print(f"Author: {book.author}")
                print(f"ISBN  : {book.isbn}")
                print(f"Status: {status}")
                return
        print("Book not found.")

    def remove_book(self):
        print("\n---- Removing a Book ----")
        title = input("Enter the title of the book to remove: ")
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{book.title}' removed successfully.")
                return
        print("Book not found.")

    def display_books(self):
        print("\n---- All Books in Library ----")
        if not self.books:
            print("No books available in the library.")
            return
        for book in self.books:
            status = f"Issued on {book.issue_date}" if book.issue_date else "Available"
            print(f"Title : {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {status}")

# Main Menu
library = Library()

while True:
    print("\n========== Library Menu ==========")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Remove Book")
    print("6. Display all Books")
    print("7. Exit")
    print("===================================")

    try:
        choice = int(input("Enter your choice (1-7): "))
    except ValueError:
        print("Please enter a valid number (1-7).")
        continue

    if choice == 1:
        library.add_book()
    elif choice == 2:
        library.issue_book()
    elif choice == 3:
        library.return_book()
    elif choice == 4:
        library.search_book()
    elif choice == 5:
        library.remove_book()
    elif choice == 6:
        library.display_books()
    elif choice == 7:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select between 1 to 7.")