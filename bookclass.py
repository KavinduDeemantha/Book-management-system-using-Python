class Book:
    def __init__(self, isbn, title, format, subject, rental, noCopies):
        self.isbn = isbn
        self.title = title
        self.format = format
        self.subject = subject
        self.rental = rental
        self.noCopies = noCopies
        

    def lend(self):
        self.noCopies -= 1
        print(f"Book {self.title} has been lent.")
        

class book:
    def __init__(self):
        self.booklist = []
        self.libraryBooks()

    def libraryBooks(self):
        book1 = Book(isbn = "ISBN1234", title = "The Solar System", format = "Hardcover", subject = "Science", rental = 15.00, noCopies = 5)
        self.booklist.append(book1)
        book2 = Book(isbn = "ISBN9876", title = "Types of Animal Species", format = "Paperback", subject = "Science", rental = 10.00, noCopies = 8)
        self.booklist.append(book2)
        book3 = Book(isbn = "ISBN1290", title = "Second World War", format = "Hardcover", subject = "History", rental = 12.50, noCopies = 1)
        self.booklist.append(book3)

    
    def add(self):
        ISBN = input("Enter ISBN number of the book: ")
        TITLE = input("Enter the title of the books: ")
        FORMAT = input("Enter the format of the book (Hardcover/Paperback): ")
        SUBJECT = input("Enter the subject of the book: ")
        RENTAL = float(input("Enter the rental price of the book: "))
        NOCOPIES = int(input("Enter the number of copies of the book: "))

        addBook = Book(isbn = ISBN, title = TITLE, format = FORMAT, subject = SUBJECT, rental = RENTAL, noCopies = NOCOPIES)
        self.booklist.append(addBook)
        print("Book added succesfully!")

    def remove(self):
        ISBN = input("Enter the ISBN number of the book you want to remove: ")
        try:
            existBooks = [book for book in self.booklist if book.isbn == ISBN]
            if len(existBooks) == 0:
                print("Error! No book with the given ISBN was found.")
                return
            else:
                for book in existBooks:
                    self.booklist.remove(book)
                print("Book removed successfully!")
        except ValueError:
            print("Error! Invalid ISBN format.")
        return
    
    def lend(self):
            isbn = input("Enter the ISBN of the book to lend: ")
            lender = input("Enter the name of the lender: ")
            for book in self.booklist:
                if book.isbn == isbn:
                    book.lend()
                    break
            else:
                print("Error! No book with the given ISBN was found.")



    def available(self):
        existBooks = list((x for x in self.booklist if x.noCopies > 0))
        if len(existBooks) > 0:
            for e in existBooks:
                print(f'ISBN NO:{e.isbn}, Title:{e.title}, Copies:{e.noCopies}')
        else:
            print("No books are available")

    def unavailable(self):
        existBooks = list((x for x in self.booklist if existBooks.noCopies <= 0))
        if len(existBooks) > 0:
            for book in existBooks:
                print(f'ISBN NO:{book.isbn}, Title:{book.title} Copies:{book.noCopies}')
        else:
            print("No books are unavailable")

    def search(self, subject):
        existBooks = list((x for x in self.booklist if x.subject == subject))
        if len(existBooks) > 0:
            for book in existBooks:
                print(f'ISBN NO:{book.isbn}, Title:{book.title}, Subject:{book.subject}, Copies:{book.noCopies}')