import pandas as pd

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
