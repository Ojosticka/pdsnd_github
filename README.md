## Date created
This project was created on the 8th of August 2020.

## Project Title
Bikeshare-project.

## Description
Bikeshare is a python project which covers a biking company located in three cities with details on their customers and locations where bikes can be rented out and returned to. This project gives detailed explanation to customers who plan to make enquiries on certain information of the datasets availaible for the three cities.

### Packages and Installation
time - python library that makes it easy to manipulate information that has to deal with date and time. Type in the terminal:  

`pip install times`

Pandas and Numpy - libraries that specifically simplifies the use of mathematical and statistical methods in python for analysing datasets. Also helps in the reading of files with extensions such as (.csv, .xlsx, .txt etc) and analyzing the tables in such datasets.

Installation - Enable to use anaconda to open the files as it already has the libraries installed in it(best ide for data science projects). If using other platforms to open the file such as pycharm or text editors(VScode, Atom), type the following commands in the terminal:  

`pip install pandas`
`pip install numpy`

### Importation 

For use on a project, this libraries must be imported.   

`import Time`
`import pandas as pd`
`import numpy as np`

**Nb:** "pd" and "np" serve as aliases for pandas and numpy

At certain points in the code, i used methods of pandas that may not be familiar, to better understand the syntax of the methods used in the code, click on the following below:

[pd.read_csv()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
[pd.to_datetime()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html)
[df[Start Time].dt.month](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.month.html)
[df[Start Time].dt.weekday_name](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.weekday.html)


### Instructions

To run the code, you will have to open up a terminal in whatever code editor you are using, once this is done, type the following command.

`python bikeshare.py`  

Once this is done, the code asks you for input on what city, month and day of data you would like to observe.  

**Nb:** For the case of city, only one city can be chosen at once from the options(chicago, new york city, washington), and for the cases of month and day, type 'all' if you want to observe data for that specific month or day.


### Files used
The files used include the bikeshare.py file which contains the code, data files with the extension(.csv) and a README file which gives details on the project and how it operates.  

..*bikeshare.py
..*chicago.csv
..*washington.csv
..*new_york_city.csv


### Functions

A breakdown of the functions used in this project and what each does is given below:  

..*`def get_filters():` Asks user to specify a city, month, and day to analyze.    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter

..*`def load_data(city, month, day):` Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day

..*`def time_stats(df):` Displays statistics on the most frequent times of travel.   
    Args: dataframe df
    returns: None  

..*`def station_stats(df):` Displays statistics on the most popular stations and trip.
    Args: dataframe df
    returns: None

..*`def seconds_convert(sec):` Converts data given in seconds to weeks, days, hours, minutes, and seconds
    Args: Takes in the seconds value to be converted from the trip_duration_stats function(int)
    returns: The converted output of the argument given.    

    The floor operator(//) gives the integer division of a division operation neglecting every number after the decimal point while the modulo operator (%) gives the integer remainder of a division operation. For more understanding of the operators, check out [this link](https://stackoverflow.com/questions/56627393/difference-between-modulus-and-floor-division-in-numpy). 

..*`def trip_duration_stats(df):` Displays statistics on the total and average trip duration.
    Args: dataframe df
    returns: None

..*`def user_stats(df):` Displays statistics on bikeshare users.
    Args: dataframe df 
    returns: None

..*`def more_info(df):` Function to ask the user if he wants to see the raw data of the information.
    Args: dataframe df
    returns: None  

..*`def main():` Gets the input data from the user from a function get_filters() and passes the result to the other      functions
    Args: None
    returns: None   


The code written at the bottom of the page:  

```if __name__ == "__main__":
    main()
```
This simply means the code was entirely ran on this module, and wasnt imported. For more information on this, check [this link](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)


## References

[stack overflow](https://stackoverflow.com/)
[Pandas dataframe documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)
[Numpy documentation](https://numpy.org/doc/stable/user/basics.html)

