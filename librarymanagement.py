import json
BOOKS_FILE = "books.json"
MEMBERS_FILE = "members.json"
class Book:
    def __init__(self, book_id, title, author, available_copies, total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available_copies = available_copies
        self.total_copies = total_copies

    def to_dict(self):
        return {
            "id": self.book_id,
            "title": self.title,
            "author": self.author,
            "available_copies": self.available_copies,
            "total_copies": self.total_copies
        }

    @staticmethod
    def from_dict(data):
        return Book(
            data["id"],
            data["title"],
            data["author"],
            data["available_copies"],
            data["total_copies"]
        )

class Member:
    def __init__(self, member_id, name, borrowed_books):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books  

    def to_dict(self):
        return {
            "id": self.member_id,
            "name": self.name,
            "borrowed_books": self.borrowed_books
        }

    @staticmethod
    def from_dict(data):
        return Member(
            data["id"],
            data["name"],
            data["borrowed_books"]
        )

class Library:
    def __init__(self):
        self.books = {}      
        self.members = {}    

        self.load_books()
        self.load_members()
        def load_books(self):
        pass

    def save_books(self):
        pass

    def load_members(self):
        pass

    def save_members(self):
        pass

    def add_book(self, book):
        pass

    def add_member(self, member):
        pass

    def borrow_book(self, member_id, book_id):
        pass

    def return_book(self, member_id, book_id):
        pass
