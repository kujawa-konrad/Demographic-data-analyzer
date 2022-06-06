# Task for FreeCodeCamp course (in progress)
# Data taken from "adult.data.csv" file

import pandas as pd

# Duplicates needs to be deleted

# Read data from file
df = pd.read_csv('adult.data.csv',
                na_values=['', '?', '-'])

# How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
race_count = df['race'].value_counts()

# What is the average age of men?
# Probably need to take 'sex' into account
average_age_men = df['age'].mean()

# What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = df['education'].value_counts(normalize=True)['Bachelors']

# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
# What percentage of people without advanced education make more than 50K?

# with and without `Bachelors`, `Masters`, or `Doctorate`
higher_education = None
lower_education = None

# percentage with salary >50K
higher_education_rich = None
lower_education_rich = None

# What is the minimum number of hours a person works per week (hours-per-week feature)?
min_work_hours = df['hours-per-week'].min()
print(min_work_hours)

# What percentage of the people who work the minimum number of hours per week have a salary of >50K?
num_min_workers = df['hours-per-week'].value_counts()[min_work_hours]

rich_percentage = (len(df[(df['salary'] == '>50K') & (df['hours-per-week'] == min_work_hours)]) / num_min_workers)*100
print(rich_percentage)

# What country has the highest percentage of people that earn >50K?
highest_earning_country = None
highest_earning_country_percentage = None

# Identify the most popular occupation for those who earn >50K in India.
top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().index[0]

