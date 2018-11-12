# [imdb_wrap](https://test.pypi.org/project/imdb-wrap/)

[![Build Status](https://travis-ci.org/SiddharthaAnand/imdb_wrap.svg?branch=master)](https://travis-ci.org/SiddharthaAnand/imdb_wrap)

[imdb_wrap](https://test.pypi.org/project/imdb-wrap/) is a python package which gives you the upcoming movies in a particular month.

## Getting Started
You can install this package using the following commands:
```
$ pip install imdb_wrap
```
Dollar sign($) before the command simply means that it is the command 
prompt of whatever command line interface you are using.

3 append operators(>>>) before the command means that it is the 
python shell which you get after typing python in your terminal 
or command line.

If you want to check out the code and contribute to this package, 
you need to have some other set of packages as pre-requisites.

### Prerequisites
You can install the required packages from requirement.txt.
```
$ pip install -r requirements.txt
```
### How to use
To get upcoming movie names:
```
>>> import imdb_wrap
>>> soup = imdb_wrap.scraper('Sep')
>>> movie_name = imdb_wrap.upcoming_movie_name(soup)
>>> print movie_name
['Tulip Fever (2017)', 'Unlocked (2017)', 'Close Encounters of the Third Kind (1977)', 'Dolores (2017)', "Viceroy's House (2017)", 'Hazlo Como Hombre (2017)', 'Ucitelka (2016)', 'Temple (2017)', 'Jackals (2017)', "I Do... Until I Don't (2017)", 'It (2017)', 'Home Again (2017)', 'Rememory (2017)', 'The Good Catholic (2017)', 'Poster Boys (2017)', '9/11 (2017)', 'In Loco Parentis (2016)', 'Trophy (2017)', 'La fille inconnue (2016)', 'Hirune-hime: Shiranai watashi no monogatari (2017)', 'Mother! (2017)', 'American Assassin (2017)', "Brad's Status (2017)", 'Rebel in the Rye (2017)', 'Because Of Gr\xc3\xa1cia (2017)', 'Carpinteros (2017)', 'In Search of Fellini (2017)', 'Kingsman: The Golden Circle (2017)', 'The LEGO Ninjago Movie (2017)', 'Battle of the Sexes (2017)', 'Friend Request (2016)', 'Victoria and Abdul (2017)', 'Stronger (2017)', 'Woodshock (2017)', 'The Tiger Hunter (2016)', 'Kongens nei (2016)', 'Bobbi Jene (2017)', 'American Made (2017)', 'Flatliners (2017)', 'Super Dark Times (2017)', 'A Question of Faith (2017)', 'Lucky (2017)', 'Take Every Wave: The Life of Laird Hamilton (2017)', 'Literally, Right Before Aaron (2017)', 'Til Death Do Us Part (2017)']
```

## Running the tests
In order to run tests, unittest module is used. To make running the tests easier, nose package is added.
nose=1.3.7 version
```
# This install the nose package in your system.
$ pip install nose
# Run this to check if the install is complete properly.
$ nosetests
``` 
After nose gets installed, go to the setup.py module and add two parameters in the setup() call.
```
setup(
	...
	test_suite='nose.collector',
	tests_require=['nose']
)
```
Now, go to the top-level package directory and run the tests:

Of course, you can add your custom-made tests inside the tests/ 
directory and then run:
```
>>> python setup.py test
```
### Break down into end to end tests
Explain what these tests test and why

```

```

### And coding style tests
Explain what these tests test and why

```
Give an example
```

## Creating your library
This command is to be run if you do not have setuptools and 
wheel installed(No need of the following installation steps if 
you have installed the packages from requirements.txt).
```
python -m pip install --upgrade setuptools wheel
```
This command will create a source distribution(tar.gz) and a built 
distribution(.whl). Newer pip versions install .whl version
but will fall back to tar.gz if needed.
```
python setup.py sdist bdist_wheel
```
Run the above command from the same directory where setup.py 
is located.
Now, you can check that there will be two new files generated 
inside dist/ directory if all went well and you see an output 
similar to the following.
```
...
adding 'imdb_wrap/__init__.py'
adding 'imdb_wrap/imdb_engine.py'
adding 'imdb_wrap/tests/__init__.py'
adding 'imdb_wrap/tests/test_imdb_engine.py'
adding 'imdb_wrap-0.1.dist-info/LICENSE'
adding 'imdb_wrap-0.1.dist-info/METADATA'
adding 'imdb_wrap-0.1.dist-info/WHEEL'
adding 'imdb_wrap-0.1.dist-info/top_level.txt'
adding 'imdb_wrap-0.1.dist-info/RECORD'
```
Congratulations! Your distribution files got created.
Now it is the time to upload your package to the official
python repository from where people all over the world can 
download your awesome package!

## Uploading to test pypi(test python packaging index)
There are two repositories named testpypi and pypi. If you are 
packaging and need a repository for testing purposes then the 
community advises to use test pypi for uploading your packages. I 
have currently used the same as my reference. The steps will be the 
same and the commands will be slightly different.

We need one last package to upload our awesome library to test python
packaging index. 
```
python pip install --upgrade twine
```
Now, the last command to upload your distribution.
```
>> twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
The repository url contains the test python packaging index url where
I have uploaded this package.
Press enter! It will ask for your username and password. Enter the same 
username and password which you have created while creating an account 
on test python packaging index.
 
## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning
This is 0.1 version of the package which was created mainly for my 
learning of creating and distributing the package through the 
python packaging index. And it was easier than I thought!

## Authors

* **Siddhartha Anand** - *Initial work* - [SiddharthaAnand](https://github.com/SiddharthaAnand)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Next Milestone
- [ ] Put in more data from imdb
- [ ] Clean and structure the code better

## References

* [Creating a python package](https://python-packaging.readthedocs.io/en/latest/minimal.html)
* [Test python packaging index - TestPyPI](https://test.pypi.org/)
* [Python packaging index - PyPI](https://packaging.python.org/tutorials/packaging-projects/)
