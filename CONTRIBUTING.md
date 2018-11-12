# [imdb_wrap](https://test.pypi.org/project/imdb-wrap/)

[![Build Status](https://travis-ci.org/SiddharthaAnand/imdb_wrap.svg?branch=master)](https://travis-ci.org/SiddharthaAnand/imdb_wrap)

[imdb_wrap](https://test.pypi.org/project/imdb-wrap/) is a python package which gives you the upcoming movies in a particular month.
If you would like to contribute to this growing package, then follow
the steps given below.

## Getting Started
Dollar sign($) before the commands used here simply means that it is the command 
prompt of whatever command line interface you are using.

3 append operators(>>>) before the command means that it is the 
python shell which you get after typing python in your terminal 
or command line.

## Setting up your machine
It is always better to use a virtual environment so that one repository 
python packages do not interfere with the other repositories. You can read 
more about it [here](https://docs.python-guide.org/dev/virtualenvs/). 
I would recommend you to install and start using virtualenv if you haven't 
started using it yet. 
```
$ source venv/bin/activate
```
The above command activates the virtual environment which I have named 
venv. After it is activated, you will see something like this in your
command prompt.
```
$ (venv) ➜  imdb_wrap git:(master)
```
Congratulations! The virtualenv and your machine is set. Now, starts two easy steps to get you all set 
for contribution.

### Prerequisites
You can install the required packages from requirement.txt.
```
$ pip install -r requirements.txt
```

* The first step is to clone the repository.
```
$ git clone https://github.com/SiddharthaAnand/imdb_wrap.git
```
* The second step is to open the repository in your favorite editor. 
The package structure is really simple and it is basically how every python
package should be. 
To read more about how to create a python package, you can [visit the tutorial](https://www.pythoncentral.io/how-to-create-a-python-package/).

Now, you are all set!

## Adding the tests
For every piece of code you add, it would be really appreciated if you add 
a unit test module/method too. It would make my and your life easier in 
finding bugs. 

In order to run tests, unittest module is used. To make running the tests 
easier, nose package is used. The testing module that you can add can be similar 
to the code written below.
```
	def test_scraper(self):
		soup = imdb_wrap.scraper('Jan')
		self.assertTrue(isinstance(soup, BeautifulSoup))

		soup = imdb_wrap.scraper('Jan', 2019)
		self.assertTrue(isinstance(soup, BeautifulSoup))

		soup = imdb_wrap.scraper(year=2019)
		self.assertTrue(isinstance(soup, BeautifulSoup))

```

Of course, you can add your custom-made tests inside the tests/ 
directory and then run:
```
>>> python setup.py test
```
Yeaaa!! You learnt how to add new tests in the package.

### Break down into end to end tests
Explain what these tests test and why

```

```

### And coding style tests
Explain what these tests test and why

```
Give an example
```

## Travis-CI/CD


## Authors

* **Siddhartha Anand** - *Initial work* - [SiddharthaAnand](https://github.com/SiddharthaAnand)

## Next Milestone
- [ ] Put in more data from imdb
- [ ] Clean and structure the code better
