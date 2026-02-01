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