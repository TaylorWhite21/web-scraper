import requests
from bs4 import BeautifulSoup

# Grabs the number of citations needed prompts
def get_citations_needed_count(url):
  citations = 0
  # grabs page information
  page = requests.get(url)
  # Parses the information
  soup = BeautifulSoup(page.content, 'html.parser')
  # Finds all <a> HTML tags.
  titles = soup.find_all('a')
  # Loops through the <a> tags and finds the citation needed text and increments by 1
  for title in titles:
    if title.text == 'citation needed':
      citations+=1
      
  return citations

def get_citations_needed_report(url):
  passages = ''
  # Next 3 lines are same as needed_count function
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  titles = soup.find_all('p')
  # Loops through found tags and appends the text if the paragraph has citation needed in it
  for title in titles:
    if 'citation needed' in title.text:
      passages += title.text
  passages = passages.replace("'\n '", ' ')
  return passages

get_citations_needed_report('https://en.wikipedia.org/wiki/Search_for_extraterrestrial_intelligence')
get_citations_needed_count('https://en.wikipedia.org/wiki/Search_for_extraterrestrial_intelligence')
