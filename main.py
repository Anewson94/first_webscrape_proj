"""
Example with BeautifulSoup
1. Install BeautifulSoup -- pip install beautifulsoup4
2. Install requests -- pip install requests
3. Install lxml -- pip install lxml
"""
"""
Reccommended order to find elements:
1. By ID
2. By class
3. By tag, CSS Selector
4. Xpath
"""

from bs4 import BeautifulSoup
import requests

# Get the website
website = "https://subslikescript.com/movie/Saving_Private_Ryan-120815"
result = requests.get(website)

# Get the text
content = result.text
# Content is a BeautifulSoup object after parsing
soup = BeautifulSoup(content, "lxml")
# print(soup.prettify())

box = soup.find("article", class_="main-article")
title = box.find("h1").get_text()

transcript = soup.find("div", class_="full-script").get_text(strip=True, separator="\n")
# print(title)
# print(transcript)

# saving script in txt file with title as the file name
# with open(f"{title}.txt", "w") as file:
#     file.write(transcript)

"""
Scraping multile pages with BeautifulSoup
"""
# root = "https://subslikescript.com"
# full_website = f"{root}/movies"
# result_two = requests.get(full_website)
# content = result_two.text
# soup_two = BeautifulSoup(content, "lxml")
# # Selecting the article holding all of the movie links
# movie_page = soup_two.find("article", class_="main-article")
# # find_all returns a list of all the links
# links = []
# for link in movie_page.find_all("a", href=True):
#     links.append(link["href"])


# for link in links:
#     full_website = f"{root}/{link}"
#     result_two = requests.get(full_website)
#     content = result_two.text
#     soup_two = BeautifulSoup(content, "lxml")

#     movie_page = soup_two.find("article", class_="main-article")

#     title_two = soup_two.find("h1").get_text()
#     transcript_two = soup_two.find("div", class_="full-script").get_text(strip=True, separator="\n")

#     with open(f"{title_two}.txt", "w") as file:
#             file.write(transcript_two)

"""
Pagination with BeautifulSoup
"""

roots = "https://subslikescript.com"
full_website_pages = f"{roots}/movies_letter-A"
result_three = requests.get(full_website_pages)
contents = result_three.text
soup_three = BeautifulSoup(contents, "lxml")

# pagination
pagination = soup_three.find("ul", class_="pagination")
pages = pagination.find_all("li", class_="page-item")
last_page = pages[2].text

for page in range(1, int(last_page) + 1):
    full_website_pages = f"{roots}movies_letter-A?{page}"
    result_three = requests.get(full_website_pages)
    contents = result_three.text
    soup_three = BeautifulSoup(contents, "lxml")

    # Selecting the article holding all of the movie links
    movie_pages = soup_three.find("article", class_="main-article")

    # find_all returns a list of all the links
    links = []
    for link in movie_pages.find_all("a", href=True):
        links.append(link["href"])


    for link in links:
        try:
            result_two = requests.get(f"{roots}/{link}")
            contents = result_two.text
            soup_two = BeautifulSoup(contents, "lxml")

            movie_pages = soup_two.find("article", class_="main-article")

            title_two = soup_two.find("h1").get_text()
            transcript_two = soup_two.find("div", class_="full-script").get_text(strip=True, separator="\n")
            with open(f"{title_two}.txt", "w") as file:
                file.write(transcript_two)
        except:
            print("Link not working")
