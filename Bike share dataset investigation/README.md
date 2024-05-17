# Bike-Sharing Dataset Investigation

This repository applies The Data Analysis Process on Bike-sharing dataset gathered from 3 different companies in the United States for last 12 Month (May 2023 - April 2024). 


![Bike-Sharing](assets/logos.png)


## Table of Contents
- [Overview of the Data](#overview)
- [Data Wrangling](#wrangling)
- [Insights](#insights)


<a id='overview'></a>
## Overview of the Data

There are 3 datasets in this project, they were gathered from 3 different companies
1. **Divvy** - Chicago, Illinois

![Divvy](assets/divvy.jpg)

Divvy is Chicagoland’s bike share system across Chicago and Evanston. It provides datasets of bike trips for public use on a monthly basis and it can be accessed [Here](https://divvybikes.com/system-data) 

2. **Citi Bike** - New York City, New York

![Citi Bike](assets/citibike.jpg)

Citi Bike is a privately owned public bicycle sharing system serving the New York City boroughs of the Bronx, Brooklyn, Manhattan, and Queens, as well as Jersey City, New Jersey. It provides datasets of bike trips for public use on a monthly basis. Its data can be accessed [Here](https://www.citibikenyc.com/system-data)

3. **Capital Bikeshare** - Washington, D.C.

![Capital Bikeshare](assets/capital_bikeshare.jpg)

Capital Bikeshare is a bicycle sharing system that serves Washington, D.C.; Arlington County, Virginia. It provides datasets of bike trips which can be accessed [Here](https://www.capitalbikeshare.com/system-data)


The nature of the data and its format underwent a lot of changes over the years. However, in the recent years, the data provided by the companies has been consistent. It contains the following columns:

- `ride_id`: unique identifier for each ride
- `rideable_type`: type of bike used for the ride
- `started_at`: date and time when the ride started
- `ended_at`: date and time when the ride ended
- `start_station_name`: name of the station where the ride started
- `start_station_id`: unique identifier for the station where the ride started
- `end_station_name`: name of the station where the ride ended
- `end_station_id`: unique identifier for the station where the ride ended
- `start_lat`: latitude of the station where the ride started
- `start_lng`: longitude of the station where the ride started
- `end_lat`: latitude of the station where the ride ended
- `end_lng`: longitude of the station where the ride ended
- `member_casual`: type of user for the ride, member for users with a membership, casual for users without a membership


<a id='wrangling'></a>
## Data Wrangling

The code involved in the data wrangling process can be found in the `wrangle_data.py` file. The data wrangling process includes the following steps:

1. **Data Collection**: The data is collected from the respective websites of the companies.

2. **Data Assessment**: The data Types, Missing Values, Duplicates, etc. are assessed. and issues were identified for the cleaning process.

3. **Data Cleaning**: The issues identified in the assessment process are cleaned. These issues involved 
    - Droping unrelevant columns
    - Fixing data types
    - Removing Outliers
    - Handling Missing Values
    - Unifying Stations' Coordinates for Further analysis 
    - Combining the 3 datasets into one dataset


<a id='insights'></a>
## Insights

**`Tableau`** was used to visualize the data and gain insights. The dashboard can be accessed below

[![Tableau Dashboard](assets/Dashboard.png)](https://public.tableau.com/views/Bike-ShareDatasetsAnalysis/Statistics?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link)

The Dashboard is fully interactive and contains filters on the following 
- City
- Month
- User Type
- Rideable Type
- Selecting Top N Stations
- Different Hours of the Day


Some of The gathered insights Are:

- For `Chicago`, As the weather gets warmer, the number of rides increases along the coast of Lake Michigan

![Chicago](assets/insight1.png)

A screenshot of the city on March 2024 (left) Vs December 2023 (right)

The duration is also generally higher along the coast of Lake Michigan regardless of the month

- For `New York City`, The number of rides is generally higher in 2 main areas of the city, South Hoboken and Grove St Path

![New York City](assets/insight2.png)

- For `Washington D.C.`, In last winter, Areas around the potamac river such as Jefferson and Lincoln Memorial had the highest number of rides. However As the weather got warmer in 2024, areas around New Hampshire started to gain popularity

![Washington D.C.](assets/insight3.png)

a screenshot of the city in late 2023 (left) Vs early 2024 (right)

notice also that the duration of rides is generally higher in areas around the potamac river regardless of the month (same as Chicago)

- Regarding the favourite hour of the day, there are 2 main peaks in the number of rides, one around 8 am in the morning and the other between 4-6 pm late in the afternoon

![Favourite Hour](assets/insight4.png)


Express more insights and customize these visualizations for different stations, months, user types, rideable types, etc. by visiting the [Dashboard](https://public.tableau.com/views/Bike-ShareDatasetsAnalysis/Statistics?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link)



