class Cd:
    def __init__(self, cdno, title, subject, rental, noCopies):
        self.cdno = cdno
        self.title = title
        self.subject = subject
        self.rental = rental
        self.noCopies = noCopies
        
    
    def lend(self):
        self.noCopies -= 1
        print(f"Lecture CD {self.title} has been lent.")

class cd:
    def __init__(self):
        self.cdlist = []
        self.libraryCds()

    def libraryCds(self):
        cd1 = Cd(cdno = 21, title = "Basics of Western Music", subject = "Music", rental = 1.50, noCopies = 11)
        self.cdlist.append(cd1)
        cd2 = Cd(cdno = 22, title = "Japanese Language", subject = "Foreign Languages", rental = 2.00, noCopies = 3)
        self.cdlist.append(cd2)
    
    def add(self):
        CDNO = input("Enter ISBN number of the book: ")
        TITLE = input("Enter the title of the books: ")
        SUBJECT = input("Enter the subject of the book: ")
        RENTAL = float(input("Enter the rental price of the book: "))
        NOCOPIES = int(input("Enter the number of copies of the book: "))

        addCd = Cd(cdno = CDNO, title = TITLE, subject = SUBJECT, rental = RENTAL, noCpies = NOCOPIES)
        self.cdlist.append(addCd)
        print("CD added succesfully!")

    def remove(self):
        CDNO = input("Enter the CD number of the CD you want to remove: ")
        try:
            existCds = [cd for cd in self.cdlist if cd.cdno == CDNO]
            if len(existCds) == 0:
                print("Error! No CD with the given CD number was found.")
                return
            else:
                for cd in existCds:
                    self.cdlist.remove(cd)
                print("CD removed successfully!")
        except ValueError:
            print("Error! Invalid CD number format.")
        return
    
    def lend(self):
            cdno = input("Enter the ISBN of the book to lend: ")
            lender = input("Enter the name of the lender: ")
            for book in self.booklist:
                if book.cdno == cdno:
                    book.lend()
                    break
            else:
                print("Error! No book with the given CD number was found.")


    def available(self):
        existCds = list((x for x in self.cdlist if x.noCopies > 0))
        if len(existCds) > 0:
            for e in existCds:
                print(f'CD NO:{e.cdno}, Title:{e.title}, Copies:{e.noCopies}')
        else:
            print("No CDs are available")

    def unavailable(self):
        existCds = list((x for x in self.cdlist if existCds.noCopies <= 0))
        if len(existCds) > 0:
            for cd in existCds:
                print(f'CD NO:{cd.cdno}, Title:{cd.title} Copies:{cd.noCopies}')
        else:
            print("No CDs are unavailable")

    def search(self, subject):
        existCds = list((x for x in self.cdlist if x.subject == subject))
        if len(existCds) > 0:
            for cd in existCds:
                print(f'CD NO:{cd.cdno}, Title:{cd.title}, Subject:{cd.subject}, Copies:{cd.noCopies}')