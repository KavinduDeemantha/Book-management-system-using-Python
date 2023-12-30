class Magazine:
    def __init__(self, magNo, title, color, subject, rental, noCopies):
        self.magNo = magNo
        self.title = title
        self.color = color
        self.subject = subject
        self.rental = rental
        self.noCopies = noCopies
        
    def lend(self):
        self.noCopies -= 1
        print(f"Magazine {self.title} has been lent.")

class magazine:
    def __init__(self):
        self.maglist = []
        self.libraryMagazines()

    def libraryMagazines(self):
        mag1 = Magazine(magNo = 1, title = "History of Cricket", color = "color", subject = "Sport", rental = 5.00, noCopies = 7)
        self.maglist.append(mag1)
        mag2 = Magazine(magNo = 2, title = "Evolution of the Computer", color = "black&white", subject = "Technology", rental = 3.00, noCopies = 21)
        self.maglist.append(mag2)
 
    def add(self):
        MAGNO = input("Enter magazine number of the magazine: ")
        TITLE = input("Enter the title of the magazine: ")
        COLOR = input("Enter the format of the magazine (color/black&white): ")
        SUBJECT = input("Enter the subject of the magazine: ")
        RENTAL = float(input("Enter the rental price of the magazine: "))
        NOCOPIES = int(input("Enter the number of copies of the magazine: "))

        addMag = Magazine(magno = MAGNO, title = TITLE, color = COLOR, subject = SUBJECT, rental = RENTAL, noCpies = NOCOPIES)
        self.maglist.append(addMag)
        print("Magazine added succesfully!")

    def remove(self):
        MAGNO = input("Enter the magazine number of the magazine you want to remove: ")
        try:
            existMag = [magazine for magazine in self.maglist if magazine.magNo == MAGNO]
            if len(existMag) == 0:
                print("Error! No magazine with the given magazine number was found.")
                return
            else:
                for magazine in existMag:
                    self.maglist.remove(magazine)
                print("magazine removed successfully!")
        except ValueError:
            print("Error! Invalid magazine number format.")
        return
    
    def lend(self):
            magNo = input("Enter the magazine number of the magazine to lend: ")
            lender = input("Enter the name of the lender: ")
            for book in self.maglist:
                if book.magNo == magNo:
                    book.lend()
                    break
            else:
                print("Error! No magazine with the given magazine number was found.")


    def available(self):
        existMag = list((x for x in self.maglist if x.noCopies > 0))
        if len(existMag) > 0:
            for e in existMag:
                print(f'Magazine NO:{e.magNo}, Title:{e.title}, Copies:{e.noCopies}')
        else:
            print("No magazines are available")

    def unavailable(self):
        existMag = list((x for x in self.maglist if existMag.noCopies <= 0))
        if len(existMag) > 0:
            for magazine in existMag:
                print(f'Magazine NO:{magazine.magNo}, Title:{magazine.title} Copies:{magazine.noCopies}')
        else:
            print("No magazine are unavailable")

    def search(self, subject):
        existMag = list((x for x in self.maglist if x.subject == subject))
        if len(existMag) > 0:
            for magazine in existMag:
                print(f'Magazine NO:{magazine.magNo}, Title:{magazine.title}, Subject:{magazine.subject}, Copies:{magazine.noCopies}')