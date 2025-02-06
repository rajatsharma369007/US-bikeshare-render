"""
This script provides functions to analyze US bikeshare data.
It allows users to filter the data by city, month, and day of the week,
and displays various statistics on the bikeshare usage.

Author: Rajat Sharma
Creation Date: 20th January 2025
"""

import time
import pandas as pd
import numpy as np

# Dictionary mapping city names to their respective data file paths
CITY_DATA = {'chicago': 'data/chicago.csv',
             'new york': 'data/new_york_city.csv',
             'washington': 'data/washington.csv'}

# List of available cities
cities = ['chicago', 'new york', 'washington']

# List of available months
months = ['january', 'february', 'march', 'april', 'may', 'june']

# List of available days of the week
days = [
    'sunday',
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday']


def get_filters():
    """Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print("Hello! Let's explore some US bikeshare data!")

    # Get user input for city (chicago, new york city, washington)
    while True:
        city = input(
            "\nWould you like to see insights for:\n- Chicago\n- New York\n- Washington\n").lower()
        if city in cities:
            break
        else:
            print('Please enter a valid city name')

    while True:
        filter = input(
            "\nWould you like to filter the data by:\n- month\n- day\n- not at all?\n").lower()
        # Get user input for month (all, january, february, ... , june)
        if filter == 'month':
            month = input(
                "\nWhich month?\n- January\n- February\n- March\n- April\n- May\n- June\n").lower()
            day = "all"
            if month in months:
                break
            else:
                print('Please enter a valid month')
        # Get user input for day of week (all, monday, tuesday, ... sunday)
        elif filter == 'day':
            day = input(
                "\nWhich day?\n- Monday\n- Tuesday\n- Wednesday\n- Thursday\n- Friday\n- Saturday\n- Sunday\n").lower()
            month = "all"
            if day in days:
                break
            else:
                print('Please enter a valid day')
        elif filter == 'not at all':
            month = "all"
            day = "all"
            break

    print(
        f"\nYou selected {city.title()}, {month.title()}, and {day.title()}.")

    print('-' * 40)
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

    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month
    if month != "all":
        # Convert month name to month number
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filter the dataframe by month
        df = df[df['month'] == month]

    # Filter by day of week
    if day != "all":
        # Filter the dataframe by day of the week
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Popular Times of Travel...\n')
    start_time = time.time()

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month from start time column to create month column
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]

    # Map month numbers to month names
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June"
    }

    # Display the most common month
    popular_month_name = month_names.get(popular_month, "Invalid month")
    print('Most Common Month: \n', popular_month_name)

    # Display the most common day of the week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common Day of the Week: \n', popular_day)

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    # Convert to 12-hour format and determine AM/PM
    period = 'AM' if popular_hour < 12 else 'PM'
    popular_hour = popular_hour % 12 or 12
    print(f'Most Common Start Hour: \n{popular_hour} {period}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most Common Start Station: \n", popular_start_station)

    # Display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most Common End Station: \n", popular_end_station)

    # Display most frequent combination of start station and end station trip
    common_combo_station = (
        df['Start Station'] +
        " to " +
        df['End Station']).mode()[0]
    print("Most Common Trip from Start to End:\n {}".format(common_combo_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_duration = df['Trip Duration'].sum()
    hours, remainder = divmod(total_duration, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(
        f"The Total Travel Time is {hours} Hours, {minutes} Minutes, and {seconds} Seconds.")

    # Display mean travel time
    average_duration = round(df['Trip Duration'].mean())
    minutes, seconds = divmod(average_duration, 60)
    if minutes > 60:
        hours, minutes = divmod(minutes, 60)
        print(
            f'The Average Travel Time is {hours} Hours, {minutes} Minutes, and {seconds} Seconds.')
    else:
        print(
            f'The Average Trip Duration is {minutes} Minutes and {seconds} Seconds.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of Each User Type:\n", user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('\nCounts of Each User Gender:\n', gender)
    else:
        print(
            f'Counts of Each User Gender:\nSorry, no gender data available for {city.title()} City')

    # Display earliest, most recent, and most common year of birth
    print('\nCounts of User Birth Year:')
    if 'Birth Year' in df.columns:
        earliest = int(df['Birth Year'].min())  # Oldest birth year
        print('Oldest User(s) Birth Year: ', earliest)

        recent = int(df['Birth Year'].max())  # Youngest birth year
        print('Youngest User(s) Birth Year: ', recent)

        common = int(df['Birth Year'].mode()[0])  # Most common birth year
        print('Most Common Birth Year: ', common)
    else:
        print(
            f'Counts of User Birth Year:\nSorry, no birth year data available for {city.title()} City')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
