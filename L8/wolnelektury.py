import requests
from bs4 import BeautifulSoup

def get_titles(html):
    soup = BeautifulSoup(html, 'html.parser')
    return [title.get_text() for title in soup.find_all('i')]

def remove_dups(lst):
    return list(set(lst))

def scrape_writers(limit = 100000000000):
    data = requests.get('https://wolnelektury.pl/api/authors/')
    authors = []

    for info in data.json():
        if not limit:
            return authors
        limit -= 1
        
        sub_url = info['href']
        detailed_info = requests.get(sub_url).json()

        books = get_titles(detailed_info['description'])
        authors.append((detailed_info['name'], remove_dups(books)))
                                     
    return authors

# pretty-print for data scraped by above function
def pp(info):
    for author_info in info:
        print(f"Most important work of {author_info[0]}: ")
        for title in author_info[1]:
            print('-> ', title)
        print('------------------------')

if __name__ == '__main__':
    a = scrape_writers(30)
    pp(a)
