from modules.library_item import LibraryItem

class Dvd(LibraryItem):
    def __init__(self, title, upc, subject, actors, director, genre):
        super().__init__(title, upc, subject)
        self.actor = actors
        self.director = director
        self.genre = genre