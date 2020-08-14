import time
import pandas as pd
import numpy as np
import loadfile

def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args: dataframe df
    returns: None """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month        
    print("\nThe most frequent month is the month of {}".format(df['month'].mode()[0] ))
    
    # Display the most common day of weekp
    print("\nThe most frequent day of the week is {}".format(df['day_of_week'].mode()[0]))
    
    # Create hour column from Start Time
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    print("\nThe most frequent start hour of bikers is: {}:00 ".format(df['hour'].mode()[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args: dataframe df
    returns: None """

    print('\nGiving you details on the Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("\nThe most frequent station bikers start from is {}".format(df['Start Station'].mode()[0]))
    
    # display most commonly used end station
    print("\nThe most frequent station bikers end is {}".format(df['End Station'].mode()[0]))
    
    # display most frequent combination of start station and end station trip 
    mode_start_end = df.groupby(['Start Station', 'End Station']).size().idxmax() #returns a tuple of the most common combination of start and end station 
    print("\nThe most popular stations bikers start and end their ride is: {}".format(mode_start_end))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def seconds_convert(sec):
    """Converts data given in seconds to years, weeks, days, hours, minutes, and seconds
        Args: sec(int)
        returns: The converted output of the argument given. """   
    
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
    print("\nThe number of each type of user is given as: \n", df['User Type'].value_counts().to_string())

    # Display counts of gender
    
    if 'Gender' in df.columns:
        print("\nThe number of counts of each gender specified is given below: \n", df['Gender'].value_counts().to_string())

    else:
        print("\nWe are sorry to inform you that we dont have availaible data for the gender of our users for the city of Washington.\n")
        
    # Display earliest, most recent, and most common year of birth
    
    # Check if the column birth year exists in the dataset
    if 'Birth Year' in df.columns:      
        #earliest birth year
        print("\nThe birth year of the oldest set of people for this dataset is: \n", int(df['Birth Year'].min()))

        #most recent year
        print("\nThe birth year of the youngest set of people for this dataset is: \n", int(df['Birth Year'].max()))

        #most popular birth year
        print("\nThe birth year of majority of our customers is: \n", int(df['Birth Year'].mode()[0]))

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
        city, month, day = loadfile.get_filters()
        df = loadfile.load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        more_info(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower().strip()
        if restart != 'yes':
            break

main()
