import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('What city of theses you would like to find about: Chicago, New York City, Washington?..\n').lower()
        if city not in CITY_DATA:
            print('please write the correct name')
        else:
             break
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('select the month: January, February, March, April, May,June? or type "all" to display all months data..\n').lower()
        months=['january','february','march','april','may','june']
        if month not in months and month != 'all':
            print('please write the correct input')
        else:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input('Select the day: Saturday,Sunday,Monday,Tuesday,Wednesday,Thursday,Friday or type "all" to display all days data..\n').lower()
        days=['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
        if day not in days and day != 'all':
            print('please write the correct input')
        else:
            break
    print('-'*40)
    return city,month, day


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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df ['Start Time']= pd.to_datetime(df['Start Time'])

    # display the most common month
    df['month']=df['Start Time'].dt.month
    common_month= df['month'].mode()[0]
    print('the most common month is :',common_month)

    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.week
    common_day= df['day_of_week'].mode()[0]
    print('the most common day of week is:',common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour= df['hour'].mode()[0]
    print('the most common start hour is:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most used start station is:', common_start)

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most used end station is:', common_end)

    # display most frequent combination of start station and end station trip
    sation_combination=(df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print('Most frequent stations combination is from:', sation_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    Sec_value= total_travel_time % (24*3600)
    hour_value= Sec_value // 3600
    print('Total travel time is: ',hour_value,'hour' )

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    Sec_value= mean_travel_time % (24*3600)
    min_value= Sec_value // 60
    print('mean travel time is: ',min_value, 'min')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('the counts of user types is: ', user_types)

    # Display counts of gender
    if 'Gender' in df:
        gender_counts=df['Gender'].value_counts()
        print('gender count is:', gender_counts)
    else:
        print('No gender information!!')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year=int(df['Birth Year'].min())
        print('The earliest birth year is:', earliest_year)
        recent_year=int(df['Birth Year'].max())
        print('The recent birth year is:', recent_year)
        common_year=int(df['Birth Year'].mode()[0])
        print('The common birth year is:', common_year)
    else:
        print('No birth year information!!')

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('the counts of user types is: ', user_types)

    # Display counts of gender
    if 'Gender' in df:
        gender_counts=df['Gender'].value_counts()
        print('gender count is:', gender_counts)
    else:
        print('No gender information!!')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year=int(df['Birth Year'].min())
        print('The earliest birth year is:', earliest_year)
        recent_year=int(df['Birth Year'].max())
        print('The recent birth year is:', recent_year)
        common_year=int(df['Birth Year'].mode()[0])
        print('The common birth year is:', common_year)
    else:
        print('No birth year information!!')

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def display_raw_data_df(df):

    raw = input('want to display the raw data? Yes or No \n').lower()
    if raw == 'yes':
        count = 0
        while True:
            print(df.iloc[count:count+5])
            count += 5
            again = input('want to see more? Yes or No \n').lower()
            if again !='yes':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data_df(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
