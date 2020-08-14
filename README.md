## Date created
This project was created on the 8th of August 2020.

## Project Title
Bikeshare-project.

## Description
Bikeshare is a python project which covers a biking company located in three cities with details on their customers and locations where bikes can be rented out and returned to. This project gives detailed explanation to customers who plan to make enquiries on certain information of the datasets availaible for the three cities.

### Packages and Installation
time - python library that makes it easy to manipulate information that has to deal with date and time. Type in the terminal:

pip install times

Pandas and Numpy - libraries that specifically simplifies the use of mathematical and statistical methods in python for analysing datasets. Also helps in the reading of files with extensions such as (.csv, .xlsx, .txt etc) and analyzing the tables in such datasets.

Installation - Enable to use anaconda to open the files as it already has the libraries installed in it(best ide for data science projects). If using other platforms to open the file such as pycharm or text editors(VScode, Atom), type the following commands in the terminal:

pip install pandas
pip install numpy

### Importation 

For use on a project, this libraries must be imported. 
`import time
 import pandas as pd
 import numpy as np`
**Nb:** "pd" and "np" serve as aliases for pandas and numpy

At certain points in the code, i used methods of pandas that may not be familiar, to better understand the syntax of the methods used in the code, click on the following below:

*[pd.read_csv()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
*[pd.to_datetime()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html)
*[df[Start Time].dt.month](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.month.html)
*[df[Start Time].dt.weekday_name](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.weekday.html)


### Instructions

To run the code, you will have to open up a terminal in whatever code editor you are using, once this is done, type the following command.

`python bikeshare.py`

Once this is done, the code asks you for input on what city, month and day of data you would like to observe.

**Nb:** For the case of city, only one city can be chosen at once from the options(chicago, new york city, washington), and for the cases of month and day, type 'all' if you want to observe data for that specific month or day.


### Files used
The files used include the bikeshare.py file which contains the code, data files with the extension(.csv) and a README file which gives details on the project and how it operates.

*bikeshare.py
*chicago.csv
*washington.csv
*new_york_city.csv

## References

*[stack overflow](https://stackoverflow.com/)
*[Pandas dataframe documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)
*[Numpy documentation](https://numpy.org/doc/stable/user/basics.html)

