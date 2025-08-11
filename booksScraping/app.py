import streamlit as st
from book_scraping import book_scaping, get_categories
categories = get_categories().keys()
selected_category = st.selectbox('select a category:', categories)

if selected_category:
    books_df = book_scaping(selected_category)
    # Better Display
    st.markdown(f"### Books in Category: {selected_category}")
    st.markdown(books_df.to_markdown(index=False))