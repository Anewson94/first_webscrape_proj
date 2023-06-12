"""
1. Install BeautifulSoup -- pip install beautifulsoup4
2. Install requests -- pip install requests
3. Install lxml -- pip install lxml
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
