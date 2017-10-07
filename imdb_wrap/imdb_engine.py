
import requests
import calendar
from bs4 import BeautifulSoup

month_num = {name:num for num, name in enumerate(calendar.month_abbr) if num}

def validate(var, type):
	pass

def create_bs(response):
	return BeautifulSoup(response.text.encode('utf-8'))

def movie_information(soup):
	movie_info_odd=soup.findAll('div', attrs={'class':'list_item odd'})
	movie_info_even=soup.findAll('div', attrs={'class':'list_item even'})
	# Combine both in one list
	return movie_info_odd, movie_info_even

def upcoming_movie_name(soup):
	movie_name_tag = soup.find_all('h4', attrs={'itemprop' : 'name'})
	movie_names = [name.text.encode('utf-8').strip() for name in movie_name_tag if name.text != None]	
	return movie_names

def upcoming_movie_description(movie_info):
	description = {}
	for movie_data in movie_info:
		movie_name = movie_data.find('h4', attrs={'itemprop':'name'}).text.encode('utf-8').strip()
		movie_desc = movie_data.find('div', attrs={'class':'outline'}).text.encode('utf-8').strip()
		description[movie_name] = movie_desc

	return description


def scraper(month='Jan'):
	if month_num[month] < 10:
		url = "http://www.imdb.com/movies-coming-soon/2017-0" + str(month_num[month])
	else:
		url = "http://www.imdb.com/movies-coming-soon/2017-" + str(month_num[month])
	try:
		response = requests.get(url)
		print response
	except Exception as e:
		pass
	soup = create_bs(response)
	# Contains all movie related information in brief
	# odd and even are nothing special, movie information are present inside both the attributes
	#movie_names = upcoming_movie_name(soup)
	#movie_info_odd, movie_info_even = movie_information(soup)
	#movie_desc = upcoming_movie_description(movie_info_odd)
	#return movie_desc
	return soup

#print scraper('Sep')
