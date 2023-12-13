"""
@author: Tejasvi Bhutiyal
"""
import pandas as pd 
import re

def count_vowels(column):
    """
    Count the number of vowels in each string of the given column.

    Args:
    column (pd.Series): A Pandas Series containing strings.

    Returns:
    list: A list containing the count of vowels in each string of the column.
    """
    numberOfVowels= []
    for i in column:
        # Use regex to find all vowels in the string
        x = re.findall("[aeiouAEIOU]", i)
        numberOfVowels.append(len(x))
    return numberOfVowels


df = pd.read_csv('titles.csv')

print('Total number of rows in file:',len(df))

#Change the column 'title' to column whose vowels you want to count
# Convert the 'title' column to string type to ensure proper vowel counting
column = df['title'].astype(str)

print('Total values in given column: ' , len(column))
numberOfvowels = count_vowels(column)

print('Displaying Number of Vowels in first 20 values of the given column:')

for i in range(20):
    print(column[i] , ':', numberOfvowels[i])

