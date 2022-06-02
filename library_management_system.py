# Library management system with all the features like adding books or removing books by admin
# borrowing a book returning a book 
# calculating fine if the borrower is late 
# updating number of copies of a book available 



from pip import main


class Library : 
    def __init__(self, l):
        self.books = l

    def ListOfAllTheBooks(self) :
        print("These are the book available in the library : ")
        for items in self.books :
            print("  *" + items)
    def CheckAvailabilityOfABook(self) :
        pass
    def BorrowABook(self, bookname) :
        self.book = bookname
        if self.book in self.books :
            print("You have been issued this book. Please return it within 30 days")
            self.books.remove(self.book)
        else :
            print("Sorry, this book is currently not available in the library")
            
      
    def ReturnABook(self, bookname) :
        self.book = bookname 

        if self.book not in self.books :
            self.books.append(self.book)
            print("Thank you for returning the book. Hope you enjoyed reading it !")
        else :
            print("we did not issue this book to anyone!!")


class Admin :
    def __init__(self, Uname, Pass, l1, l2 ) :
        self.bookslist = l1
        self.booksdata = l2
        self.id = Uname 
        self.password = Pass
        if self.id != "Saurabh" or self.password != "12345" :
            print("You don't have admin access !!")
            exit()

        


    def AddNewBooks(self) :
       newBook = input("Enter the name of the book you want to add in the library : ")
       if newBook not in self.booksdata :
           self.bookslist.append(newBook)
           self.booksdata.append(newBook)
           print("Book has been successfully added to the libary. Thank you !!")
       else :
           print("We already have this book!")
             
        
    def RemoveABook(self) : 
        removeBook = input("Enter the name of the book you want to remove from the library : ")
        if removeBook in self.booksdata :
           self.bookslist.remove(removeBook)
           self.booksdata.remove(removeBook)
           print("Book has been successfully removed from the libary. Thank you !!")
        else :
           print("We do not have this book!")

class Student :
    def __init__(self, l):
        self.books = l
    def SearchABook(self, bookname) :
        self.book = bookname 
        if self.book in self.books :
            print("This book is available in the Library")
        else :
            print("Sorry, This book is currently not available in the library...")
            
   

if __name__ == '__main__' :
    print(''' ====== Welcom To The Prayagraj Central Library ====== 
    Please choose an option : 
    1. List All The Books
    2. Search A Book
    3. Borrow A Book
    4. Return A Book
    5. Admin Access
    6. Exit
    ''')
    listOfBooks = ["DSA", "Algorithm", "Maths", "Hindi", "Science", "Digital Electronics", "c++"]
    booksData = ["DSA", "Algorithm", "Maths", "Hindi", "Science", "Digital Electronics", "c++"]
    lab = Library(listOfBooks)
    
    student = Student(listOfBooks)
    while(True) :
        try :
            SelectAnOption = int(input("Choose your option : "))
            if SelectAnOption == 1 :
                lab.ListOfAllTheBooks()
            elif SelectAnOption == 2 :
                bookname = input("Enter the name of the book : ")
                student.SearchABook(bookname)
            elif SelectAnOption == 3 :
                bookname = input("Enter the name of the book you want to borrow : ")
                lab.BorrowABook(bookname)
                
            elif SelectAnOption == 4 :
                bookname = input("Enter name of the book you want to return : ")
                if bookname in booksData : 
                    lab.ReturnABook(bookname)
                else :
                    print("This book does not belongs to this library!")
            elif SelectAnOption == 5 :
                Username = input("Enter User name : ")
                Password = input("Enter Password : ")
                admin = Admin(Username, Password, listOfBooks, booksData)

                if Username != "Saurabh" or Password != "12345" :
                    print("You don't have admin access !!")
                    break
                else :
                    print(''' === Hello Admin ===
                    Please choose an option : 
                    1. Add new books
                    2. Remove a book
                    ''')
                    SelectAdminOptions = int(input("Choose one option : "))
                    if SelectAdminOptions == 1 :
                        admin.AddNewBooks()
                    elif SelectAdminOptions == 2 :
                        admin.RemoveABook()
                    else :
                        print("Invalid Option Selected!!")
   
            elif SelectAnOption == 6 :
                print("Thank you for using Prayagraj Library Management System. Hope you enjoyed it !!")
                exit()
            else :
                print("Invalid Option Selected!! Select Correct Option :")
            
        except ValueError :
            print("Please Enter An Integer Value !!!")
