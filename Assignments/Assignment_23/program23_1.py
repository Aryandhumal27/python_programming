# 1. Write a Python program to implement a class named BookStore with the following specifications:
#   -> The class should contain two instance variables:
#       -> Name (Book Name)
#       -> Author (Book Author)
#   -> The class should contain one class variable:
#       -> NoOfBooks (initialize it to 0)
#   -> Define a constructor (init that accepts Name and Author and initializes instance variables.
#   -> Inside the constructor, Increment the class Variable NoOfBooks by 1 whenever a new object is created.
#   -> Implement an instance method:
#       -> Display() should display book details in the format: 
#       <BookName> by <Author>. No of books: <NoOfBooks>
#   -> Example usage:
#       -> Obj1 BookStore ("Linux System Programming", "Robert Love") 
#          Objl.Display() books: 1 Linux System Programming by Robert Love. No of books : 1
#       -> Obj2 BookStore("C Programming", "Dennis Ritchie") 
#          Obj2.Display() #C Programming by Dennis Ritchie. No of books: 2


class BookStore:
    NoOfBooks = 0

    def __init__(self, name, author):
        self.Name = name
        self.Author = author
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of Books : {BookStore.NoOfBooks}")

def main():
    obj1 = BookStore("Linux System Programming", "Robert Love")
    obj1.Display()

    obj2 = BookStore("C Programmimg", "Dennis Ritchie")
    obj2.Display()

    print("End of main")

if __name__ == "__main__":
    main()
 