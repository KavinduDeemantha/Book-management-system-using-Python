from bookclass import book
from magazineclass import magazine
from dvdclass import dvd
from cdclass import cd

fbook = book()
fmagazine = magazine()
fedudvd = dvd()
fleccd = cd()

def menu():
    choice = -1
    while choice != 0:
        print('''
        -----------WELCOME TO MY LIBRARY MANAGEMENT SYSTEM-----------

        CHOOSE WHAT YOU WANT!

        1 - Books
        2 - Magazines
        3 - Educational DVDs
        4 - Lecture CDs
        5 - Search resources by subject
        0 - Quit
        
        --------------------------------------------------------------
        ''')

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Invalid choice!")

        if choice == 1 or choice == 2 or choice == 3 or choice == 4:
            second_menu(choice)

        elif choice == 5:
            sub = input("Enter the subject you need to search by:  ")
            fbook.search(sub)
            fmagazine.search(sub)
            fedudvd.search(sub)
            fleccd.search(sub)
        
        elif choice == 0:
            quit()

def second_menu(choice):
    if choice == 1:
        resource = "book"
        todo = fbook
    elif choice == 2:
        resource = "magazine"
        todo = fmagazine
    elif choice == 3:
        resource = "educational DVD"
        todo = fedudvd
    elif choice == 4:
        resource = "lecture CD"
        todo = fleccd

    choice2 = -1
    while choice2 != 0:
        print(f"Press 1 to add a {resource}")
        print(f"Press 2 to remove a {resource}")
        print(f"Press 3 to view available {resource}")
        print(f"Press 4 to view unavailable {resource}")
        print(f"Press 5 to lend a {resource}")
        print("Press 6 to go to Main menu")
        print("Press 0 to quit")

        try:
            choice2 = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid Choice!")

        if choice2 == 1:
            todo.add()
        elif choice2 == 2:
            todo.remove()
        elif choice2 == 3:
            todo.available()
        elif choice2 == 4:
            todo.unavailable()
        elif choice2 == 5:
            todo.lend()
        elif choice2 == 6:
            menu()
            break
        elif choice2 == 0:
            quit()

menu()