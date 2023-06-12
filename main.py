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

print(title)

print(transcript)
