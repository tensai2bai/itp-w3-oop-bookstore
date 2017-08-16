class Bookstore(object):
    def __init__(self,storeName):
        self.name = storeName
        self.books = []
    
    def get_books(self):
        return self.books    
    
    def add_book(self,book):
        self.books.append(book)

    def search_books(self, title=None, author=None):
        result = []
        for book in self.books:
            if book.author == author:
                result.append(book)
            elif book.title == title:
               result.append(book)
            elif title and book.title.lower().startswith(title.lower()):
                result.append(book)
        return result

class Author(object):
    def __init__(self,name,nation):
        self.name = name
        self.nationality = nation
        self.books = []
    
    def get_books(self):
        return self.books 


class Book(object):
    def __init__(self,title,author):
        self.title = title
        self.author = author
        author.books.append(self)
