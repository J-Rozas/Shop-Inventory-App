from models.book import Book
from models.publisher import Publisher

from repositories import publisher_repository, book_repository

book_repository.delete_all()
publisher_repository.delete_all()

publisher1 = Publisher("Penguin Random House", "United States", "1745 Broadway, New York, NY 10019")
publisher_repository.add(publisher1)

publisher2 = Publisher("Hachette Livre", "France", "8 Rue d'Assas, 75006 Paris")
publisher_repository.add(publisher2)

book1 = Book("Ulysses", 730, "Modernist novel", "James Joyce", 10, publisher1, 35.99)
book_repository.add(book1)

book2 = Book("The Great Gatsby", 163, "Historical fiction", "F. Scott Fitzgerald", 6, publisher2, 17.85)
book_repository.add(book2)

book3 = Book("To the Lighthouse", 320, "Fiction novel", "Virginia Woolf", 3, publisher1, 16.99)
book_repository.add(book3)

book4 = Book("Nineteen Eighty-Four", 328, "Science fiction", "George Orwell", 0, publisher2, 10.00)
book_repository.add(book4)