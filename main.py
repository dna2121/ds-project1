from modules.library_item import LibraryItem
from modules.book import Book
from modules.cd import Cd
from modules.dvd import Dvd
from modules.magazine import Magazine
from modules.catalog import Catalog

import json

f = open('files/data.json')
data_json = json.load(f)

list_book = []
list_cd = []
list_magazine = []
list_dvd = []

for item in data_json:
    if item['source'] == 'book':
        list_book.append(Book(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            isbn=item['issbn'],
            authors=item['authors'],
            dds_number=item['dds_number']
        ))
    elif item['source'] == 'magazine':
        list_magazine.append(Magazine(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            volume=item['volume'],
            issue=item['issue']
        ))
    elif item['source'] == 'dvd':
        list_dvd.append(Dvd(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            actors=item['actors'],
            directors=item['directors'],
            genre=item['genre']
        ))
    elif item['source'] == 'cd':
        list_cd.append(Cd(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            artist=item['artist']
        ))
        
catalog_all = [list_book, list_magazine, list_cd, list_dvd]

input_search = 'test'
results = Catalog(catalog_all).search(input_search)

print ('\n\n=====| HASIL SEARCH |=====\n')
for index, result in enumerate(results):
    print(f'result ke {index+1} | {result}\n')
print('=====================================\n\n')