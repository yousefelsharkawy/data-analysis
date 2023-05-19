import time
import pandas as pd
import numpy as np

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
        city = input("Please Choose The Name of the city: chicago, new york city or washington \n").lower()
        if city in CITY_DATA:
            break
        else:
            print("Please re-Enter a valid input and check the spelling!")

    # get user input for month (all, january, february, ... , june)
    months = ['January', 'February', 'March', 'April', 'May', 'June',"All"]
    while True:
        month = input("Please Select a month of the following: January, February, March, April, May, June or all \n").title()
        if month in months:
            break
        else:
            print("Please re-Enter a valid input and check for spelling!")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','All']
    while True:
        day = input("Please Select a day: Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or all \n").title()
        if day in days:
            break
        else:
            print("Please re-Enter a valid input and check for spelling!")
        
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
    df = pd.read_csv(CITY_DATA[city])
    # Seprate months, days and hours into new columns
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month_name()
    df["day"] = df["Start Time"].dt.day_name()
    df["hour"] = df["Start Time"].dt.hour
    
    # Filter the data by month if requested
    if month != "All":
        df = df[df["month"] == month]
    # Filter the data by day if requested 
    if day != "All":
        df = df[df["day"] == day]
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    total = df.shape[0]
    # display the most common month
    if month == 'All' and day == "All":
        # Display the most common month 
        common_month = df["month"].mode()[0]
        print("The Most Common month of renting the Bikes is: {} with the count of {} of total {}".format(common_month, df[df["month"] == common_month].count()[0], total))

        # display the most common day of week
        common_day = df["day"].mode()[0]
        print("The most common day of renting the bikes is: {} with the count of {} of total {} ".format(common_day, df[df["day"] == common_day].count()[0], total))

        # display the most common start hour
        common_hour = df["hour"].mode()[0]
        print("The most common hour of renting the bikes is {} with the count of {} of total {}".format(common_hour, df[df["hour"] == common_hour].count()[0], total))
    
    elif (month != "All") and (day == "All"):
        # display the most common day of week
        common_day = df["day"].mode()[0]
        print("The most common day of renting the bikes in {} is: {} with the count of {} of total {}".format(month, common_day, df[df["day"] == common_day].count()[0], total))

        # display the most common start hour
        common_hour = df["hour"].mode()[0]
        print("The most common hour of renting the bikes in {} is {} with the count of {} of total {}".format(month, common_hour, df[df["hour"] == common_hour].count()[0], total))
    
    elif month == "All" and day != "All":
        common_month = df["month"].mode()[0]
        print("The Most Common month of renting the Bikes in {} is: {} with the count of {} of total {}".format(day, common_month, df[df["month"] == common_month].count()[0], total))
        
        common_hour = df["hour"].mode()[0]
        print("The most common hour of renting the bikes in {} is {} with the count of {} of total {}".format(day,common_hour, df[df["hour"] == common_hour].count()[0], total))
    
    else:
        common_hour = df["hour"].mode()[0]
        print("The most common hour of renting the bikes in {} of {} is {} with the count of {} of total {}".format(day,month,common_hour, df[df["hour"] == common_hour].count()[0], total))

        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The Most common used start Station is: {}".format(df["Start Station"].mode()[0]))

    # display most commonly used end station
    print("The Most common used end Station is: {}".format(df["End Station"].mode()[0]))    

    # display most frequent combination of start station and end station trip
    start_and_end_most = df['Start Station'] + "and" +  df['End Station']
    start_and_end_most = start_and_end_most.mode()[0]
    print("The  most frequent combination of start station and end station trip: {}\n".format(start_and_end_most))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The Total Travel Time based on your requested information is aproximatelly {} seconds or {} hours".format(int(df["Trip Duration"].sum()), int(df["Trip Duration"].sum()/3600) ))

    # display mean travel time
    print("The Average of The Travel Time is {} seconds or {} minutes".format(int( df["Trip Duration"].mean() ), int( df["Trip Duration"].mean()/60 )  ))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print("The Counts Of The User Types are: {} \n".format(user_type))
    
    # Display counts of gender
    if 'Gender' in df:
        Gender = df['Gender'].value_counts()
        print("The Counts Of Each Gender are: {} \n".format(Gender))        

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = df["Birth Year"].min()
        recent = df["Birth Year"].max()
        most_common = df['Birth Year'].value_counts().index[0]
        count = df['Birth Year'].value_counts().iloc[0]
        print("The oldest person to rent a bike based on your requested information was born in {}".format(earliest))
        print("The Youngest person to rent a bike was born in {}".format(recent))
        print("The Most common year of birth to rent a bike is {} with the counts of {} people".format(most_common,count))
        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """displays data based on the request of the user 5 rows at a time"""
    answer = input("Would you like to see 5 rows of the data you requested? Type yes or no \n").lower()
    if answer == 'yes':
        maximum = df.shape[0]
        i = 0
        while True:
            if (i+5) < maximum:
                print(df.iloc[i:(i+5)])
                i += 5
            else:
                df.iloc[i:maximum]
                print("You have reached the End of the data!")
                break
            answer = input("Would you like to display another 5 rows? Yes or no \n").lower()
            if answer == "no":
                break
    
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
