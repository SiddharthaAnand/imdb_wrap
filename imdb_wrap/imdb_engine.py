
import requests
from bs4 import BeautifulSoup
def scrape(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text)
	movie_name_tag = soup.find_all('h4', attrs={'itemprop' : 'name'})
	movie_names = [name.text.encode('utf-8').strip() for name in movie_name_tag if name.text != None]
	return movie_names

