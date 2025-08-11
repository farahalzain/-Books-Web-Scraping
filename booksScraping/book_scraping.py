import requests
from bs4 import BeautifulSoup
import pandas as pd
import math

def get_categories():
    base_url = "https://books.toscrape.com"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'lxml')
    categories = soup.find('ul', class_='nav nav-list').find('ul').find_all('li')
    categories_cleaned = [category.a.text.strip() for category in categories]
    categories_simplified = [category.lower().replace(" ","-")+'_'+str(i+1) for i, category in enumerate(categories_cleaned)]
    categories_dict = {k:v for k,v in zip(categories_cleaned, categories_simplified)}
    return categories_dict

def get_category_url(category):
    base_url = 'https://books.toscrape.com/catalogue/category/books/'
    category_key = get_categories().get(category)  
    if category_key:
        return f'{base_url}{category_key}/index.html', category_key
    else:
        raise ValueError(f'Category {category} is not found in the dictionary')

def book_scaping(category):
    try:
        url, category_key = get_category_url(category)
    except ValueError as e:
        print(e)
        return pd.DataFrame()
    else:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        
        form_tag = soup.find('form', class_='form-horizontal')
        
        if form_tag:
            total_num_of_books = int(form_tag.find('strong').text)
        else:
            total_num_of_books = len(soup.find_all('h3'))
        
        no_of_each_page = 20
        no_of_pages = math.ceil(total_num_of_books / no_of_each_page)

        all_books = pd.DataFrame()

        for page in range(1, no_of_pages + 1):
            if page == 1:
                page_url = url
            else:
                page_url = f"https://books.toscrape.com/catalogue/category/books/{category_key}/page-{page}.html"

            response = requests.get(page_url)
            soup = BeautifulSoup(response.content, 'lxml')

            names = [name.a.get("title") for name in soup.find_all('h3')]
            prices_cleaned2 = [price.text[1:] for price in soup.find_all('p', class_='price_color')]
            rates = [rating["class"][1] for rating in soup.find_all('p', class_='star-rating')]
            rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
            ratings_cleaned = [rating_map.get(rating) for rating in rates]

            df_book = pd.DataFrame({
                'Book Name': names,
                'Price': prices_cleaned2,
                'Rating': ratings_cleaned
            })

            all_books = pd.concat([all_books, df_book], ignore_index=True)

        return all_books


