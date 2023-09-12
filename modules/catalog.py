from modules.book import Book
from modules.cd import Cd
from modules.dvd import Dvd
from modules.magazine import Magazine

class Catalog():
    def __init__(self, catalog=None):
        self.catalog = catalog
        
    def search(self, input_search):
        list_result = []
        for catalog in self.catalog:
            for item in catalog:
                if input_search.lower() in item.title.lower():
                    if type(item) == Book:
                        list_result.append(f'Title : {item.title} | Type Catalog : Book')
                    elif type(item) == Magazine:
                        list_result.append(f'Title : {item.title} | Type Catalog : Magazine')
                    elif type(item) == Dvd:
                        list_result.append(f'Title : {item.title} | Type Catalog : DVD')
                    elif type(item) == Cd:
                        list_result.append(f'Title : {item.title} | Type Catalog : CD')
                    else:
                        pass
                 
        return list_result