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
