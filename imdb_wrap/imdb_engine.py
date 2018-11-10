
import requests
import calendar
from bs4 import BeautifulSoup

month_num = {name:num for num, name in enumerate(calendar.month_abbr) if num}


def create_bs(response):
	return BeautifulSoup(response.text.encode('utf-8'))


def upcoming_movie_name(soup):
	movie_names = []
	movie_name_tag = soup.find_all('h4')
	for _movie in movie_name_tag:
		_movie_result = _movie.find_all('a')
		try:
			_movie_name = _movie_result[0]['title']
			movie_names.append(_movie_name)
		except KeyError as e:
			continue
	return movie_names


def scraper(month='Jan', year=2019):
	if month_num[month] < 10:
		url = "http://www.imdb.com/movies-coming-soon/{year}-0{month}".format(year=year, month=month_num[month])
	else:
		url = "http://www.imdb.com/movies-coming-soon/{year}-{month}".format(year=year, month=month_num[month])
	try:
		response = requests.get(url)
		print response
	except Exception as e:
		print e
	soup = create_bs(response)
	return soup

