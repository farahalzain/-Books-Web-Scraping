# Book Scraping Project

## Overview

This project scrapes book data from [Books to Scrape](https://books.toscrape.com) and displays it in an interactive **Streamlit dashboard**.

You can extract details such as:

* Book Name
* Price (£)
* Rating (1-5)
* Availability (In stock)

It allows users to:

* Select a book category from a sidebar
* View a table of books in that category
* Download the data as CSV
* See basic statistics (total books, average price)
* Visualize rating distribution

---

## Features

* Web scraping using `requests` and `BeautifulSoup`
* Data handling with `pandas`
* Interactive dashboard with `Streamlit`
* Automatic handling of multiple pages per category
* CSV download for each category
* Plotting ratings distribution with `matplotlib`


## Usage
## Run the Streamlit dashboard

```bash
streamlit run app.py
```

* The dashboard will open in your browser
* Select a category from the sidebar to view books
* Download the data as CSV or view statistics and charts

### Example Python usage

```python
from book_scraping import book_scraping, get_categories

categories = list(get_categories().keys())
print("Available categories:", categories)

books_df = book_scraping("Science")  # Replace with your chosen category
print(books_df.head())
```

---

## Project Structure

```
book-scraping/
│── book_scraping.py       # Web scraping logic
│── app.py                 # Streamlit dashboard
```
---
