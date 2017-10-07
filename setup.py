from setuptools import setup

setup(name="imdbwrap",
	  version="0.1",
	  description="Imdb: collection of movies",
	  url="https://github.com/SiddharthaAnand/imdb_wrap",
	  author="siddhartha",
	  author_email="siddharthalibra13@gmail.com",
	  license="MIT",
	  packages=['imdb_wrap'],
	  test_suite='nose.collector',
	  tests_require=['nose'],
	  zip_safe=False)