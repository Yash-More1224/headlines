import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL) # python object that stores HTML data sent by server

_html = page.text # static site content

# print(len(_html.split("\n"))) # number of lines in the html

soup = BeautifulSoup(page.content, "html.parser") 
# we use .content instead of .text to have character encoding in bytes

results = soup.find(id="ResultsContainer")
# print(results.prettify())

job_cards = results.find_all("div", class_="card-content")

# count = 0
# for card in job_cards:
#     count += 1
#     print(card, end=f"\ncount={count}\n\n\n")

for job_card in job_cards:
    title_element = job_card.find("h2", class_="title") # is also a BeatifulSoup object
    company_element = job_card.find("h3", class_="company")
    location_element = job_card.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip()) # .strip() removes extra while spaces
    print()


# filtering software jobs:
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

# getting all relevent info of these python jobs: (by getting parent of the "h2" elements)
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_cards = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# extracting attributes from html elements, sq. bracket is used:
for job_card in python_job_cards:
    links = job_card.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")

# but we are looking for the 2nd url, so:
for job_card in python_job_cards:
    links = job_card.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")
