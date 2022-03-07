from requests import get
from bs4 import BeautifulSoup
header={
        'Accept-Language': 'en-US'
    }
url = 'https://www.imdb.com/list/ls046118590/?ref_=tt_rels_4'
response = get(url, headers=header)
scrapedPage = BeautifulSoup(response.text, 'html.parser')

starwars_movies = []
film_containers = scrapedPage.find_all('div', class_='lister-item-content')
for film_content in film_containers:
    film_header = film_content.find_all('h3', class_='lister-item-header')
    runtime = film_content.find('span', class_='runtime').string
    ipl_rating = film_content.find('span', class_='ipl-rating-star__rating').string
    metascore = film_content.find('span', class_='metascore').string
    paragraphs = film_content.find_all('p')
    description = paragraphs[1].string.strip()
    director = paragraphs[2].a.string
    for film in film_header:
        title = film.find('a', text=True).string
        year = film.find('span', class_='lister-item-year').string
        film_details = [title, year, director, runtime, ipl_rating, metascore, description]
        starwars_movies.append(film_details)
        
import pandas as pd 
all_starwars_films = pd.DataFrame(starwars_movies,
                                 columns = ['film', 'year', 'director', 'runtime', 'ipl_rating', 'metascore', 'description'])
all_starwars_films
