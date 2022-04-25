class Book:
    def __init__(self, input_title, input_number_of_pages, input_genre, input_author, input_stock, input_publisher, input_selling_price, input_id = None):
        self.id = input_id
        self.title = input_title
        self.number_of_pages = input_number_of_pages
        self.genre = input_genre
        self.author = input_author
        self.stock = input_stock
        self.publisher = input_publisher
        self.selling_price = input_selling_price