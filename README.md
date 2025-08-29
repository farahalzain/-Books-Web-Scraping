# News API Project

This project allows you to fetch **top news headlines** from [NewsAPI](https://newsapi.org/) based on **keywords** and **countries**.
It uses Python with `requests` and supports environment variables (`.env`) for API key security.

---

## Features

* Fetch top headlines by **keyword** (e.g., `AI`, `sports`, `economy`).
* Fetch top headlines by **country** (e.g., `us`, `gb`, `in`).
* Fetch headlines by **keyword + country** together.
* Secure API key management using `.env` file.

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/news-api-project.git
   cd news-api-project
   ```

2. Install required dependencies:

   ```bash
   pip install requests python-dotenv
   ```

3. Create a `.env` file in the root directory and add your **API key**:

   ```
   API_KEY=your_api_key_here
   ```

  Get your API key from [https://newsapi.org/](https://newsapi.org/).

---

## Usage

Run the script:

```bash
python main.py
```

Example interaction:

```
API key loaded successfully.
Enter a keyword (e.g., AI, sports, economy): ai
******* Headline 1 *******
Source:
	ID: None
	Name: BBC News
Title: AI is transforming technology
Author: John Smith
URL: https://www.bbc.com/news/ai-article

********************************
Enter a country (e.g., us, gb, in): us
******* Headline 1 *******
Source:
	ID: cnn
	Name: CNN
Title: US election and AI debates
Author: Jane Doe
URL: https://www.cnn.com/politics/article
```

---

## Project Structure

```
news-api-project/
│── main.py        # Main script
│── .env           # Store API key (not shared publicly)
│── README.md      # Project documentation
```
