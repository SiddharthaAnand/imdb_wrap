import setuptools

setuptools.setup(name="imdb_wrap",
      version="0.1",
      description="Imdb: collection of movies",
      url="https://github.com/SiddharthaAnand/imdb_wrap",
      author="siddhartha",
      author_email="siddharthalibra13@gmail.com",
      license="MIT",
      packages=setuptools.find_packages(),
      test_suite='nose.collector',
      tests_require=['nose'],
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      install_requires=['bs4', 'requests'],
      zip_safe=False,
     classifiers=[
                 "Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent",
                  ],
     )
