import time
import pandas as pd
import numpy as np
import json

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Defines the list of valid inputs for cities, months and weekdays

cities=['chicago','new york city','washington']
months=['all','january','february','march','april','may','june','july','august','september','october','november','december']
days=['all','monday','tuesday','wednesday','thursday','friday','saturday']
    
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
   
     # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city=input('Enter the name of the city to analyze the data:').lower()
        while city in cities:
        
         # TO DO: get user input for month (all, january, february, ... , june)

            month=input('Enter the name of the month to filter by, or "all" to apply no month filter:').lower()
            while month in months:
            
                # TO DO: get user input for day of week (all, monday, tuesday, ... sunday) 
                day=input('enter the name of the day of week to filter by, or "all" to apply no day filter:').lower()
                if day in days:
                    break
                else:
                    print('wrong weekday')
                    continue
                break        
            else:
                print('wrong month')
                continue
            break
        else:
            print('wrong city name')
            continue
        print('input registered')    
        break
    
            

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
    
    df=pd.read_csv(CITY_DATA[city])
    
    # Convert the 'Start_time' datatype to datetime format

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from 'Start_Time' column to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # Filter data by month

    if month != 'all':
        month =  months.index(month) + 1
        df = df[ df['month'] == month ]

    # Filter data by day of week

    if day != 'all':

        # Filter by day of week to create the new dataframe

        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    most_common_month=df['Start Time'].dt.month.value_counts().idxmax()
    print("The most common month of travel is : {}".format(most_common_month))


    # TO DO: display the most common day of week
    
    most_common_weekday=df['Start Time'].dt.weekday_name.value_counts().index[0]
    print("The most common weekday is : {}" .format(most_common_weekday))
   


    # TO DO: display the most common start hour
    
    most_common_hour=df['Start Time'].dt.hour.value_counts().index[0]
    print("The most common hour of travel is : {} ".format(most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    count1=df.groupby(['Start Station']).size().sort_values(ascending=False)
    print("Most commonly used start station is {}".format(count1.index[0]))


    # TO DO: display most commonly used end station

    count2=df.groupby(['End Station']).size().sort_values(ascending=False)
    print("Most commonly used end station is {} ".format(count2.index[0]))


    # TO DO: display most frequent combination of start station and end station trip
    
    count3=df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)
    print("Most frequent combination is {}".format(count3.index[0]))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    #Converts the time to datetime format and calculates travel duration for each row
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['tra_time']=(df['End Time']-df['Start Time']).astype('timedelta64[s]')


    # TO DO: display total travel time
    
    tot_tra_time=df['tra_time'].sum()
    print("Total travel time is {}:".format(tot_tra_time))
    
    
    # TO DO: display mean travel time
    
    mean_tra_time=df['tra_time'].mean()
    print("Mean travel time is {}:".format(mean_tra_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_count=df.groupby(['User Type']).size().sort_values(ascending=False)
    print("The user count is {}".format(user_count))


    # TO DO: Display counts of gender
    
    if 'Gender' in df.columns:
    
        print("Counts of gender:\n")

        gender_counts = df['Gender'].value_counts()
   
    else :
        print('"Gender data not available for this particular city"')



    # TO DO: Display earliest, most recent, and most common year of birth
    
    if 'Birth Year' in df.columns:

        earliest=df['Birth Year'].min()
        print("Earliest birth year is {}".format(earliest))
    
        most_recent=df['Birth Year'].max()
        print("Most recent birth year is {}".format(most_recent))
    
        most_common_birth_year=df.groupby(['Birth Year']).size().sort_values(ascending=False).index[0]
        print("Most common birth year is {}".format(most_common_birth_year))


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        
    else :
        print("'Birth year data not available for this paricular city'")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(df):

    """If the user wants to examine raw data , it displays first five rows of raw bikeshare data to the users ."""

    row_length = df.shape[0]

    # iterate from 0 to the number of rows in steps of 5

    for i in range(0, row_length, 5):

        yes = input('\nWould you like to examine 5 lines of raw trip data? Type \'yes\' or \'no\'\n> ')
        if yes.lower() != 'yes':
            break

        # retrieve and convert data to json format

        # split each json row data 

        row_data = df.iloc[i: i + 5].to_json(orient='records', lines=True).split('\n')

        for row in row_data:

            # pretty print each user data

            parsed_row = json.loads(row)

            json_row = json.dumps(parsed_row, indent=2)

            print(json_row)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
