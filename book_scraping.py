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
    categories_simplified = [category.lower().replace(" ", "-") + '_' + str(i + 1) for i, category in enumerate(categories_cleaned)]
    return {k: v for k, v in zip(categories_cleaned, categories_simplified)}


def get_category_url(category):
    base_url = 'https://books.toscrape.com/catalogue/category/books/'
    category_key = get_categories().get(category)
    if category_key:
        return f'{base_url}{category_key}/index.html', category_key
    else:
        raise ValueError(f'Category {category} is not found.')


def book_scraping(category):
    try:
        url, category_key = get_category_url(category)
    except ValueError as e:
        print(e)
        return pd.DataFrame()

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')

    # Total books in category
    form_tag = soup.find('form', class_='form-horizontal')
    total_books = int(form_tag.find('strong').text) if form_tag else len(soup.find_all('h3'))

    books_per_page = 20
    pages = math.ceil(total_books / books_per_page)

    all_books = pd.DataFrame()

    rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

    for page in range(1, pages + 1):
        page_url = url if page == 1 else f"https://books.toscrape.com/catalogue/category/books/{category_key}/page-{page}.html"

        response = requests.get(page_url)
        soup = BeautifulSoup(response.content, 'lxml')

        names = [name.a.get("title") for name in soup.find_all('h3')]
        prices = [price.text[1:] for price in soup.find_all('p', class_='price_color')]
        rates = [rating["class"][1] for rating in soup.find_all('p', class_='star-rating')]
        ratings = [rating_map.get(r) for r in rates]
        availability = [avail.text.strip() for avail in soup.find_all("p", class_="instock availability")]

        df_books = pd.DataFrame({
            'Book Name': names,
            'Price (£)': prices,
            'Rating (1-5)': ratings,
            'Availability': availability
        })

        all_books = pd.concat([all_books, df_books], ignore_index=True)

    return all_books
