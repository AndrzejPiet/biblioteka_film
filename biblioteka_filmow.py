class Film :
    def __init__ (self, title, year, genre):

        self.title=title
        self.year = year
        self.genre = genre

        self._plays = 0

    def play(self, step=1):
        self._plays += step

    @property
    def current_play(self):
        return self._plays

    def to_dict(self):
        return {
            "title": self.title,
            "year": self.year,
            "genre": self.genre,
            "film_play": self._plays,
        }


   def __str__(self):
        return f'Aktualna biblioteka filmow : {self.title} rok produkcji {self.year} typ filmu : {self.genre}'

class Series(Film):
    def __init__(self, episode,season, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.episode = episode
        self.season = season

        self._plays = 0

    def play(self, step=1):
        self.plays += step

    @property
    def current_play(self):
        return self._plays
    def to_dict(self):
        return {
            "title": self.title,
            "year": self.year,
            "genre": self.genre,
            "plays": self._plays,
            "episode": self.episode,
            "season": self.season,
        }

    def __str__(self):
        return f'Aktualna biblioteka seriali : {self.title} rok wydania {self.year} ' \
               f'typ filmu : {self.genre} odcinek : {self.episode} sezon : {self.season}'

class Library :
    def __init__(self, name: str):
        self.name = name
        self._list = {}

    def add_product(self, product: Film):
        selected_product = self._list.get(product.title)
        if selected_product:
            selected_product.episode += product.episode
            if selected_product.price:
                logging.warning(f"{product.plays} price changed to {product.plays}")
            selected_product.plays = product.plays
            self._list[product.title] = selected_product
            return selected_product
        else:
            self._list[product.name] = product
            return product

    def add_products(self, products):
        for product in products:
            self.add_product(product)

    def visualise_library(self):
        print("-----------------")
        for product_value in self._list.values():
            print(product_value)







if __name__ == '__main__':

    Library.add_products([
        Series(
              title="apple",
              genre=1,
              episode=10),
        Product('a', 1, 10),
        Product('b', 1, 10),
        Product('c', 1, 10),
        Product('d', 1, 10)
    ])

    Library.visualise_library()

