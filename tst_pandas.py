# Data manipulation and analysis library for working with structured data.such as tables of numerical and textual data

# Pandas provides two main data structures: Series and DataFrame. A Series is a one-dimensional array-like object that can hold any data type. It has an associated index, which labels each element in the Series. A DataFrame is a two-dimensional table-like structure that contains rows and columns of data. It is similar to a spreadsheet or a SQL table. Each column in a DataFrame is a Series.

# Pandas provides a wide range of functions for reading and writing data to and from various file formats, including CSV, Excel, SQL databases, and more. It also provides functions for data cleaning, filtering, sorting, merging, and grouping.

# Here are some examples of what you can do with Pandas:
#     Load data from a CSV file into a DataFrame
#     Filter and sort data in a DataFrame based on certain criteria
#     Compute summary statistics of the data, such as mean, median, and standard deviation
#     Aggregate data using group-by operations
#     Visualize data using built-in plotting functions

# Creating a Pandas DataFrame:
import pandas as pd

data = {
    'name':['Alvine', 'Bob', 'Breve'],
    'age': [25, 30, 35],
    'city':['new york', 'los angeles', 'chicago']
}

df = pd.DataFrame(data)
print(df)

# Reading data from a CSV file into a Pandas DataFrame:
# df = pd.read_csv('dt.csv')

# Selecting data from a Pandas DataFrame:
df = pd.DataFrame(data)
print(df['name']) 
print(df[['name', 'age']])
print(df.loc[0])
print(df['age'] > 30)

# Adding a new column to a Pandas DataFrame:
df['salary'] = [5000, 5000, 70000]
print(df)

# Grouping data in a Pandas DataFrame:
df = pd.DataFrame(data)
grouped = df.groupby('name')['age'].mean()
print(grouped)