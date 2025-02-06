class Library:
    # Constructor to initialize the books list
    def __init__(self):
        self.books = []  # Initialize an empty list to store book titles

    # Method to add a new book to the list
    def add_book(self, title):
        self.books.append(title)  # Adds the book title to the list

    # Method to search for a book by its title
    def search_by_title(self, title):
        if title in self.books:  # Check if the title exists in the books list
            print(f"'{title}' is available in the library.")
            return True
        else:
            print(f"'{title}' is not found in the library.")
            return False

    # Method to print all book titles in the library
    def display_books(self):
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("No books in the library.")


# Main method to interact with the Library class
def main():
    # Create a Library object
    my_library = Library()

    # Add books to the library
    my_library.add_book("1984 by George Orwell")
    my_library.add_book("To Kill a Mockingbird by Harper Lee")
    my_library.add_book("Pride and Prejudice by Jane Austen")

    # Display all books in the library
    my_library.display_books()

    # Search for a book by title
    my_library.search_by_title("1984 by George Orwell")  # Book is in the library
    my_library.search_by_title(
        "Moby Dick by Herman Melville"
    )  # Book is not in the library


# Call the main method to run the program
if __name__ == "__main__":
    main()
