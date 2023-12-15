"""
@author: Tejasvi Bhutiyal
"""
import pandas as pd 
import re

def count_vowels(s):
    """
    Count the number of vowels in a string.

    Args:
    s (str): A string.

    Returns:
    int: The count of vowels in the string.
    """
    return len(re.findall('[aeiouAEIOU]', s))

# Read data from file
df = pd.read_csv('titles.csv')

# Ensure the 'title' column is of string type
df['title'] = df['title'].astype(str)

# Apply the function to count vowels in the 'title' column
df['vowel_count'] = df['title'].apply(count_vowels)

# Display the DataFrame
print(df.head(20))