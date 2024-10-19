def interface():
    print("_________________________________")
    print(" -LIBRARY APPLICATION MENU- ")
    print("List all the books in the library --> 1 (WORKING)")
    print("List all the books that are checked out --> 2 (WORKING)")
    print("Add a new book --> 3 (WORKING)")
    print("Delete a book --> 4 (WORKING)")
    print("Search a book by ISBN number --> 5 (WORKING)")
    print("Search a book by name --> 6 (WORKING)")
    print("Check out a book to a student --> 7 (NOT WORKING)")
    print("List all the students --> 8 (WORKING)")
    print("Exit --> e")
    print("_________________________________")

def mainMenu():
    tasks = [listBooks,checkoutBooks,addBooks,deleteBooks,searchISBN,searchBookName,7,listStudents]
    while True:
        interface()
        option = input("🔎Choose a option:")
        option = option.strip()
        if option.lower() == "e":
            break
        else:
            try:
                option = int(option)
                if 1<= option <= 8:
                    tasks[option-1]()
                else:
                    print("Invalid option!")
            except ValueError:
                print("Invalid option !, try again with numbers from 1 to 8")




def listBooks():
    with open("books.txt", "r", encoding= "utf8")as f:
        content = f.read()
        print("---------------------------------")
        print(content)
        print("---------------------------------")

def checkoutBooks():
    with open("books.txt", "r",encoding= "utf8") as f:

        for line in f.readlines():
            values = line.split(",")
            if values[3].strip() == "T":
                print("---------------------------------")
                print(line.strip())
        print("---------------------------------")
def addBooks():
    emptyList = []
    with open("books.txt", "r",encoding= "utf8")as f:
        for line in f:
            items = line.split(",")
            emptyList.append(items[0])
    isbnNumber = input("ISBN Number or Press r to Return Main Menu: ").strip()
    if isbnNumber.lower() == "r":
        mainMenu()

    with open("books.txt", "a",encoding= "utf8")as f:
        if isbnNumber not in emptyList:
            bookName = input("Book Name: ").strip()
            author = input("Author Name: ").strip()
            checkedout = "F"
            f.write(f"{isbnNumber},{bookName},{author},{checkedout}\n")
        else:
            print("This book already exists")
            addBooks()




def deleteBooks():
    isbnNumber = input("ISBN Number or Press r to Return Main Menu").strip()
    if isbnNumber.lower() == "r":
        mainMenu()


    with open("books.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    found = False
    for i in range(len(lines)):
        line = lines[i]
        items = line.split(",")
        if items[0] == isbnNumber and items[3].strip() == "F":
            lines.pop(i)
            found = True
            print(f"{isbnNumber} was deleted successfully!")
            break

    if not found:
        print(f"{isbnNumber} not found!")

    with open("books.txt", "w", encoding="utf-8") as file:
        file.writelines(lines)


def searchISBN():
    while True:
        isbn = input("Enter ISBN Number or Press r to Return Main Menu: ")
        isbn = isbn.strip()

        if isbn.lower() == "r":
            mainMenu()


        with open("books.txt", "r",encoding= "utf8") as f:

            for line in f:
                values = line.split(",")
                if values[0].strip() == isbn.strip():
                    print("---------------------------------")
                    print(line)
                    print("---------------------------------")
                    break
            else:
                print("Not Found try again")
                searchISBN()



def searchBookName():
    while True:
        name = input("Enter a Book Name or Press r to Return Main Menu: ")
        name = name.strip()
        if name.lower() == "r":
            mainMenu()

        with open("books.txt", "r",encoding= "utf8") as f:

            for line in f:
                values = line.split(",")
                if values[1].strip() == name:
                    print("---------------------------------")
                    print(line)
                    print("---------------------------------")
                    break

            else:
                print("Not Found. Please try again.")


def listStudents():
    with open("students.txt", "r",encoding= "utf8") as f:
        content = f.read()
        print("---------------------------------")
        print(content)
        print("---------------------------------")



mainMenu()





