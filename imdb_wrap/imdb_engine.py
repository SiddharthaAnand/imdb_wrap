
import requests
from bs4 import BeautifulSoup

def scrape(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text)
	movie_name_tag = soup.find_all('h4', attrs={'itemprop' : 'name'})
	movie_names = [name.text.encode('utf-8').strip() for name in movie_name_tag if name.text != None]
	return movie_names

if __name__ == '__main__':
	print "Enter the number of month for which you want the movies: "
	month = raw_input()
	url = "http://www.imdb.com/movies-coming-soon/2017-" + month

	names = scrape(url)
	for number, name in enumerate(names):
		print number+1, name


