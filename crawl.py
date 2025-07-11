from bs4 import BeautifulSoup
import requests

URL = "https://www.bbc.com/news"

try:
    page = requests.get(URL)
    # print("got page")
    # print(page.text)

    soup = BeautifulSoup(page.content, "html.parser")
    try: 
        headlines = soup.find_all("h2", class_="sc-9d830f2a-3 jqQlce")
        sub_headlines = soup.find_all("h2", class_="sc-9d830f2a-3 fWzToZ")
        most_watched = soup.find_all("h2", class_="sc-9d830f2a-3 UijWH")

        # print("\n\nMain Headlines:\n\n")
        # for i, news in enumerate(headlines):
        #     print(f"{i+1}. {news.text.strip()}")
        
        # print("\n\nSmaller Headlines:\n\n")
        # for i, news in enumerate(sub_headlines):
        #     print(f"{i+1}. {news.text.strip()}")

        # print("\n\nMost watched:\n\n")
        # for i, news in enumerate(most_watched):
        #     print(f"{i+1}. {news.text.strip()}")

    except: 
        print("error fetching headlines")
except Exception as e:
    print(f"error occured : {e}")

# next: web interface using streamlit, vader sentiment analysis, search using key-words