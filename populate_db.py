from models.book import Book
from models.publisher import Publisher

from repositories import publisher_repository

publisher1 = Publisher("Penguin Random House", "United States", "1745 Broadway, New York, NY 10019, United States")
publisher_repository.add(publisher1)

publisher2 = Publisher("Hachette Livre", "France", "8 Rue d'Assas, 75006 Paris, France")
publisher_repository.add(publisher2)
