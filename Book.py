class Book:
    def __init__(self, title, author, isbn, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Isbn: {self.isbn}")
        print(f"Genre: {self.genre}")
        print("-" * 20, "\n")
        
book1 = Book("The alchemist", "Paulo Coelho", "978-0062315007", "Fiction")
book2 = Book("Clean Code", "Robert c.Martin", "978-0132350884", "Programming")
book3 = Book("To Kill a mocking bird", "Harper Lee", "978-0061120084", "Classic")

print("-" *4 ,"Library Books","-" *4)
book1.display_info()
book2.display_info()
book3.display_info()

        