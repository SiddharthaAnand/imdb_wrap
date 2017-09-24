# imdb_wrap

A python package which gives you the upcoming movies in a particular month.

## Getting Started

You can simply install this package using the following commands:

### Prerequisites

You need the following packages

```
requests
bs4
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

To get the movie description:
```
>>> movie_info_odd, movie_info_even = imdb_wrap.movie_information(soup)
>>> movie_desc = imdb_wrap.upcoming_movie_description(movie_info_odd)
```

Pick any movie name from the list printed above
```
>>> print movie_desc['Tulip Fever (2017)']
An artist falls for a young married woman while he's commissioned to paint her portrait during the Tulip mania of 17th century Amsterdam.
```

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

## Authors

* **Siddhartha Anand** - *Initial work* - [SiddharthaAnand](https://github.com/SiddharthaAnand)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Next Milestone
* Put in more data from imdb
* Clean and structure the code better

## References

* [Creating a python package](https://python-packaging.readthedocs.io/en/latest/minimal.html)
