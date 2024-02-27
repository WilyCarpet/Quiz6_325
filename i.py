class Management:
    def addBook(self,book):
        raise NotImplementedError
    def removeBook(self,book):
        raise NotImplementedError
    def generateReport(self):
        raise NotImplementedError

class Normal:
    def searchBookByTitle(self):
        raise NotImplementedError

    def searchBookByAuthor(self):
        raise NotImplementedError

    def searchBookByGenre(self):
        raise NotImplementedError

class Registered(Normal):
    def borrowBook(self,book):
        raise NotImplementedError
    
    def returningBook(self, book):
        raise NotImplementedError
    
class Libraian(Management,Normal):
    def addBook(self,book):
        self.bookList.append(book)
    
    def removeBook(self, book):
        if book in self.bookList:
            self.bookList.remove(book)
    
    def generateReport(self):
        print(self.report)
    
    def searchBookByTitle(self):
        print("Books sorted Title")

    def searchBookByAuthor(self):
        print("Books sorted by Author")

    def searchBookByGenre(self):
        print("Books sorted by Genre")

class Guest(Normal):
    def searchBookByTitle(self):
        print("Books sorted Title")

    def searchBookByAuthor(self):
        print("Books sorted by Author")

    def searchBookByGenre(self):
        print("Books sorted by Genre")

class RegisteredUser(Registered):
    def searchBookByTitle(self):
        print("Books sorted Title")

    def searchBookByAuthor(self):
        print("Books sorted by Author")

    def searchBookByGenre(self):
        print("Books sorted by Genre")

    def borrowBook(self, book):
        if book in self.bookList:
            book.borrowed = True
        else:
            print("Book not in library")
    
    def returningBook(self, book):
        if book in self.bookList:
            book.borrowed = False
        else:
            print("Book doesn't belong to library")