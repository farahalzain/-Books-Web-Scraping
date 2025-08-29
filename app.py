import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from book_scraping import book_scraping, get_categories

# Sidebar - category selector
st.sidebar.title("Book Scraper")
categories = get_categories().keys()
selected_category = st.sidebar.selectbox("Select a category:", categories)

if selected_category:
    st.markdown(f"## Books in Category: *{selected_category}*")
    books_df = book_scraping(selected_category)

    if not books_df.empty:
        # Display dataframe
        st.dataframe(books_df)

        # Download button
        csv = books_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name=f"{selected_category}_books.csv",
            mime="text/csv"
        )

        # Statistics
        st.markdown("### Statistics")
        books_df["Price (£)"] = pd.to_numeric(books_df["Price (£)"], errors="coerce")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Books", len(books_df))
        with col2:
            st.metric("Average Price (£)", round(books_df["Price (£)"].mean(), 2))

        # Chart: Distribution of ratings
        st.markdown("### Ratings Distribution")
        fig, ax = plt.subplots()
        books_df["Rating (1-5)"].value_counts().sort_index().plot(kind="bar", ax=ax)
        ax.set_xlabel("Rating")
        ax.set_ylabel("Count")
        st.pyplot(fig)

    else:
        st.warning("No books found in this category.")
