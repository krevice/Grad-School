import pandas as pd
import math

# PART 1

# Read titles.csv file, replace '\N' values with NaN values, and save new .csv
titles_df = pd.read_csv("titles.csv", na_values=['\\N'])
titles_df.replace('\\N', math.nan, inplace=True)
titles_df.to_csv('titles_cleaned.csv', index=False)

# Read people.csv file, replace '\N' values with NaN values, and save new .csv
people_df = pd.read_csv("people.csv", na_values=['\\N'])
people_df.replace('\\N', math.nan, inplace=True)
people_df.to_csv('people_cleaned.csv', index=False)

# Read cast.csv file, replace '\N' values with NaN values, and save new .csv
cast_df = pd.read_csv("cast.csv", na_values=['\\N'])
cast_df.replace('\\N', math.nan, inplace=True)
cast_df.to_csv('cast_cleaned.csv', index=False)


# Creating the category.csv file
#Create 'category' dataframe
category_df = cast_df[['category']].dropna()

# Filter unique categories
unique_names = category_df['category'].unique()

# Create new column title
category_df = pd.DataFrame(unique_names, columns=['CATEGORY_NAME'])

# Alphabetize the category values
category_df = category_df.sort_values('CATEGORY_NAME')

# Reset the index of the dataframe
category_df = category_df.reset_index(drop=True)

# Create CATEGORY_ID column
category_df['CATEGORY_ID'] = range(1, len(category_df) + 1)

# Reordering columns
category_df = category_df[['CATEGORY_ID', 'CATEGORY_NAME']]

# Create category.csv file
category_df.to_csv('category.csv', index=False)

# Updating cast_cleaned.csv with using CATEGORY_ID values
# Create dictionary mapping CATEGORY_IDs to CATEGORY_NAMEs
category_map = category_df.set_index('CATEGORY_NAME')['CATEGORY_ID'].to_dict()

# Replace category with CATEGORY_ID and create new cast_updated.csv file
cast_df['category'] = cast_df['category'].replace(category_map)
cast_df.to_csv('cast_updated.csv', index=False)

# PART 2

import sqlite3
import csv

# Function to read .csv files we want to create tables for
def read_csv(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        data = []
        for row in reader:
            data.append(tuple(row.values()))
        return data

# Conect to SQLite database
con = sqlite3.connect('imdb.db')
cursor = con.cursor()

# Create titles table
titles_data = read_csv('titles_cleaned.csv')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS titles (
        tconst TEXT,
        ordering INTEGER,
        title TEXT,
        region TEXT,
        language TEXT,
        isOriginalTitle INTEGER
    )
''')
cursor.executemany('''
    INSERT INTO titles VALUES (?, ?, ?, ?, ?, ?)
''', titles_data)

# Create productions table
productions_data = read_csv('productions.csv')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productions (
        tconst TEXT,
        titleType TEXT,
        primaryTitle TEXT,
        originalTitle TEXT,
        startYear INTEGER,
        endYear INTEGER,
        runtimeMinutes INTEGER,
        genre TEXT
    )
''')
cursor.executemany('''
    INSERT INTO productions VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', productions_data)

# Create ratings table
ratings_data = read_csv('ratings.csv')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ratings (
        tconst TEXT,
        averageRating REAL,
        numVotes INTEGER
    )
''')
cursor.executemany('''
    INSERT INTO ratings VALUES (?, ?, ?)
''', ratings_data)

# Create people table
people_data = read_csv('people_cleaned.csv')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS people (
        nconst TEXT,
        primaryName TEXT,
        birthYear INTEGER,
        deathYear INTEGER,
        primaryProfession TEXT,
        knownForTitles TEXT
    )
''')
cursor.executemany('''
    INSERT INTO people VALUES (?, ?, ?, ?, ?, ?)
''', people_data)

# Create cast table
cast_data = read_csv('cast_cleaned.csv')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cast (
        tconst TEXT,
        ordering INTEGER,
        nconst TEXT,
        category TEXT,
        job TEXT,
        characters TEXT
    )
''')
cursor.executemany('''
    INSERT INTO cast VALUES (?, ?, ?, ?, ?, ?)
''', cast_data)

# Commit changes and close connection
con.commit()
con.close()
