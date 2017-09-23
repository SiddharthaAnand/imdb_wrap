
import requests
import calendar
from bs4 import BeautifulSoup

month_num = {name:num for num, name in enumerate(calendar.month_abbr) if num}

def scrape(month='Jan'):
	if month_num[month] < 10:
		url = "http://www.imdb.com/movies-coming-soon/2017-0" + str(month_num[month])
	else:
		url = "http://www.imdb.com/movies-coming-soon/2017-" + str(month_num[month])
	response = requests.get(url)
	soup = BeautifulSoup(response.text)
	movie_name_tag = soup.find_all('h4', attrs={'itemprop' : 'name'})
	movie_names = [name.text.encode('utf-8').strip() for name in movie_name_tag if name.text != None]
	return movie_names
