class Dvd:
    def __init__(self, dvdno, title, subject, rental, noCopies):
        self.dvdno = dvdno
        self.title = title
        self.subject = subject
        self.rental = rental
        self.noCopies = noCopies
    
    def lend(self):
        self.noCopies -= 1
        print(f"Educational DVD {self.title} has been lent.")

class dvd:
    def __init__(self):
        self.dvdlist = []
        self.librarydvds()

    def librarydvds(self):
        dvd1 = Dvd(dvdno = 10, title = "Birth of the Solar System", subject = "Astronomy", rental = 2.50, noCopies = 10)
        self.dvdlist.append(dvd1)
        dvd2 = Dvd(dvdno = 11, title = "Pythagoras Theorem", subject = "Math", rental = 1.00, noCopies = 50)
        self.dvdlist.append(dvd2)
    
    def add(self):
        DVDNO = input("Enter DVD number of the DVD: ")
        TITLE = input("Enter the title of the DVD: ")
        SUBJECT = input("Enter the subject of the DVD: ")
        RENTAL = float(input("Enter the rental price of the DVD: "))
        NOCOPIES = int(input("Enter the number of copies of the DVD: "))

        addDvd = Dvd(DVDNO = DVDNO, title = TITLE, subject = SUBJECT, rental = RENTAL, noCpies = NOCOPIES)
        self.dvdlist.append(addDvd)
        print("DVD added succesfully!")

    def remove(self):
        DVDNO = input("Enter the DVD number of the DVD you want to remove: ")
        try:
            existDvds = [dvd for dvd in self.booklist if dvd.dvdno == DVDNO]
            if len(existDvds) == 0:
                print("Error! No DVD with the given DVD was found.")
                return
            else:
                for dvd in existDvds:
                    self.dvdlist.remove(dvd)
                print("DVD removed successfully!")
        except ValueError:
            print("Error! Invalid DVD number format.")
        return
    
    def lend(self):
            dvdno = input("Enter the ISBN of the book to lend: ")
            lender = input("Enter the name of the lender: ")
            for book in self.dvdlist:
                if book.dvdno == dvdno:
                    book.lend()
                    break
            else:
                print("Error! No book with the given ISBN was found.")


    def available(self):
        existDvds = list((x for x in self.dvdlist if x.noCopies > 0))
        if len(existDvds) > 0:
            for e in existDvds:
                print(f'DVD NO:{e.dvdno}, Title:{e.title}, Copies:{e.noCopies}')
        else:
            print("No DVDs are available")

    def unavailable(self):
        existDvds = list((x for x in self.dvdlist if existDvds.noCopies <= 0))
        if len(existDvds) > 0:
            for dvd in existDvds:
                print(f'DVD NO:{dvd.dvdno}, Title:{dvd.title} Copies:{dvd.noCopies}')
        else:
            print("No DVDs are unavailable")

    def search(self, subject):
        existDvds = list((x for x in self.dvdlist if x.subject == subject))
        if len(existDvds) > 0:
            for dvd in existDvds:
                print(f'ISBN NO:{dvd.dvdno}, Title:{dvd.title}, Subject:{dvd.subject}, Copies:{dvd.noCopies}')