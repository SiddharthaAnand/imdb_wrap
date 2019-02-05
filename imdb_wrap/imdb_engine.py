
import requests
import calendar
from bs4 import BeautifulSoup

month_num = {name:num for num, name in enumerate(calendar.month_abbr) if num}
base_url = "http://www.imdb.com/movies-coming-soon/"


def create_bs_object(response):
	"""
	Creates a BeautifulSoup object with response received.
	:param response: HTML response from IMDB server
	:return: BeautifulSoup response object
	"""
	return BeautifulSoup(response.text.encode('utf-8'),  "html.parser")


def upcoming_movie_name(soup):
	"""
	Extracts the list of movies from BeautifulSoup object.
	:param soup: BeautifulSoup object containing the html content.
	:return: list of movie names
	"""
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
	"""
	Sends a request to IMDB server to fetch upcoming movies.
	:param month: Month for which you want the movies.
	:param year: year for which you want the movies.
	:return: BeautifulSoup object containing the Response from IMDB.
	"""
	if month_num[month] < 10:
		url = base_url + "{year}-0{month}".format(year=year, month=month_num[month])
	else:
		url = base_url + "{year}-{month}".format(year=year, month=month_num[month])
	try:
		response = requests.get(url)
	except Exception as e:
		print e
	return create_bs_object(response)

