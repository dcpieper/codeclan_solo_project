class Game:

    def __init__(self, title, developer, publisher, genre, wholesale, price, stock, id=None):
        self.title = title
        self.developer = developer
        self.publisher = publisher
        self.genre = genre
        self.wholesale = wholesale
        self.price = price
        self.stock = stock
        self.id = id

    def price_markup(self):
        price_markup = self.price - self.wholesale
        return price_markup