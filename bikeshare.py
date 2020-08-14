import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months_letters = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    name_of_person = input('Hello! My name is ojo, what\'s yours(letters only please), let\'s explore some US city bikeshare data!: ').strip()
       
    print("\noh wow {}, that\'s such a beautiful name you got there\n".format(name_of_person))
            
            
    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:        
        city = " ".join(input("Hi {}, what city would you like to check, data is only availaible for the cities: (chicago, new york city, washington),please endeavour to choose from these options, cant choose more than one city at a time: ".format(name_of_person)).lower().split())
        
        if city in CITY_DATA.keys():   
            print("\nHmmm cool choice, {} it is then\n".format(city))
            break     
        else:
            print("\nOuch an error occurred, please check your choice again, could be a typo, do try again\n")

    # Get user input for month (all, january, february, ... , june)
    while True:
        month = input("Hi {}, what month would you like to get data for? Nb: type 'all' if you want data for all the six months, if not, enter a specific  month(ranges from january to june), e.g january:  ".format(name_of_person)).lower().strip()
        if month in months_letters or month == 'all':
                
            if month == 'may':
                print('\nsuper psyched, you chose my birth month\n')
            else:     
                print("\nHmmm cool choice, {} it is then\n".format(month))   
            break
        else:
            print("\nOuch an error occurred, please check your choice again, could be a typo, ensure they are all letters and no apostrophe('') involved, why dont you try again\n")

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("{}, what day of the week are you interested in? Nb: type 'all' if you want data for all the days of the week, if not, enter a specific day(ranges from monday to sunday): ".format(name_of_person)).lower().strip()
            
        if day in days or day == 'all':
            print("\nHmmm cool choice, {} it is then\n".format(day))
            break
        else:
            print("\nOuch an error occurred, please check your choice again, could be a typo, ensure they are all letters and no apostrophe('') involved, and try again.\n")

    print('-'*40)
    return city, month, day

            
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #loads the data of the city entered 
    df = pd.read_csv(CITY_DATA[city]) 
    
    #Converts the datatype of the start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])    
    
    #extracting the day and month from the start time column to create new columns
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    dict_months_letters = {i+1:j for i,j in enumerate(months_letters)}
    df['month'] = df['month'].replace(dict_months_letters)
    
    #filtering the data to the users choice for month and day of week
    if month != 'all':
        df = df[df['month'].isin([month])]
        
    if day != 'all':
        day = day.title()
        df = df[df['day_of_week'].isin([day])]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args: dataframe df
    returns: None """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    mode_letter = df['month'].mode()[0]           
    print("\nThe most frequent month is the month of {}".format(mode_letter))
    
    # Display the most common day of weekp
    frequent_day = df['day_of_week'].mode()[0]
    print("\nThe most frequent day of the week is {}".format(frequent_day))
    
    # Display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print("\nThe most frequent start hour of bikers is: {}:00 ".format(popular_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args: dataframe df
    returns: None """

    print('\nGiving you details on the Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("\nThe most frequent station bikers start from is {}".format(popular_start_station))
    
    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("\nThe most frequent station bikers end is {}".format(popular_end_station))
    
    # display most frequent combination of start station and end station trip 
    mode_start_end = df.groupby(['Start Station', 'End Station']).size().idxmax() #returns a tuple of the most common combination of start and end station 
    print("\nThe most popular stations bikers start and end their ride is: {}".format(mode_start_end))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def seconds_convert(sec):
    """Converts data given in seconds to weeks, days, hours, minutes, and seconds
        Args: Takes in the seconds value to be converted from the trip_duration_stats function(int)
        returns: The converted output of the argument given. """
    
     #Input given in seconds; convert to years, weeks, days, hour, minute, and seconds format
    
    years = sec//(52*7*24*3600)
    sec %= (52*7*24*3600)
    weeks = sec//(7*24*3600)
    sec %= (7*24*3600)
    days = sec//(24*3600)
    sec %= (24*3600)
    hours = sec//3600
    sec %= 3600
    minutes = sec//60
    sec %= 60
    seconds = sec
    
    return "%dyear(s) %dweek(s) %dday(s) %dhour(s) %dminute(s) %dsecond(s) " % (years, weeks, days, hours, minutes, seconds)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args: dataframe df
    returns: None """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
   
    tot_travel_time = int(df['Trip Duration'].sum())
    
    print("\n The sum of the time travelled for each ride gives: \n", seconds_convert(tot_travel_time))
    
    # display mean travel time
    
    avg_travel_time = int(df['Trip Duration'].mean())

    print("\n The average travel time of a biker to end a trip is: \n", seconds_convert(avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.
    Args: dataframe df 
    returns: None """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count_types = df['User Type'].value_counts().to_string()
    print("\nThe number of each type of user is given as: \n", user_count_types)

    # Display counts of gender
    
    # Check if column Gender exists in the dataset
    if 'Gender' in df.columns:
        Gender_count = df['Gender'].value_counts().to_string()
        print("\nThe number of counts of each gender specified is given below: \n", Gender_count)

    else:
        print("\nWe are sorry to inform you that we dont have availaible data for the gender of our users for the city of Washington.\n")
        
    # Display earliest, most recent, and most common year of birth
    
    # Check if the column birth year exists in the dataset
    if 'Birth Year' in df.columns:
        
        #earliest birth year
        Earliest_birth_year = int(df['Birth Year'].min())
        print("\nThe birth year of the oldest set of people for this dataset is: \n", Earliest_birth_year)

        #most recent year
        recent_birth_year = int(df['Birth Year'].max())
        print("\nThe birth year of the youngest set of people for this dataset is: \n", recent_birth_year)

        #most popular birth year
        Popular_birth_year = int(df['Birth Year'].mode()[0])
        print("\nThe birth year of majority of our customers is: \n", Popular_birth_year)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        
    else:
        print("\nSo sorry, the information for year of birth is unavailaible for the city of Washington.\n")

def more_info(df):
    """Function to ask the user if he wants to see the raw data of the information.
    Args: dataframe df
    returns: None. """
    
    
    i = 5
    while True:
            
        answer = input("\nWould you like to observe the first few rows of the raw data of the city based on your specifications or keep viewing the next set of rows in the dataset, type 'yes' to proceed or 'no' if you are not interested: ").lower().strip()              
                       
        if answer == 'yes':
            print("\n", df.iloc[i-5:i])
            i += 5                                     
                  
        elif answer == 'no':           
            print("\nThank you for your time, hope you enjoyed the service, my name remains ojo, have a nice day!\n")
            break
            
        else:
            print("\nLooks like you made a slight typo error, please try again.") 
                
def main():
    """
    Gets the input data from the user from a function get_filters() and passes the result to the other functions
    Args: None
    returns: None """
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        more_info(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower().strip()
        if restart != 'yes':
            break


if __name__ == "__main__":
    main()
