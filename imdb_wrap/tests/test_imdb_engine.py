from unittest import TestCase
from bs4 import BeautifulSoup
import imdb_wrap

class TestEngine(TestCase):
	def test_scraper(self):
		soup = imdb_wrap.scraper('Jan')
		self.assertTrue(isinstance(soup, BeautifulSoup))