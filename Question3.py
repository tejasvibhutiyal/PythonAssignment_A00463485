"""
@author: Tejasvi Bhutiyal
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# Sample data to show the format expected from the user
sampleData = [["John", 76], ["Kumar", 54], ["Zoey", 51]]
df = pd.DataFrame(sampleData, columns=("Name", "Age"))

# Set up the title and subheader of the Streamlit app
st.title('Assignment: Question 3')
st.subheader('Upload the file in this format')

# Display the sample data as a table
st.table(df)

# File uploader for the user to upload their CSV file
uploaded_file = st.file_uploader(label="Choose a CSV file to upload")

if uploaded_file is not None:
    # Check if the file is a CSV based on its filename
    if uploaded_file.name.lower().endswith('.csv'):
        dataframe = pd.read_csv(uploaded_file)

        # Check if the required columns 'Name' and 'Age' are in the DataFrame
        if {'Name', 'Age'}.issubset(dataframe.columns):
            if dataframe['Name'].dtype == 'object':
                if dataframe['Age'].dtype in ['int64', 'int32', 'int16', 'int8']:
                    bins = np.arange(dataframe['Age'].min(), dataframe['Age'].max() + 2) - 0.5

                    # Set up the histogram plot
                    st.subheader('Histogram of Age Data:')
                    fig, ax = plt.subplots()
                    dataframe['Age'].hist(bins=bins, ax=ax, rwidth=0.8)
                    ax.set_title('Histogram of Age Column')
                    ax.set_xlabel('Age')
                    ax.set_ylabel('Frequency')
                    ax.set_xticks(np.arange(dataframe['Age'].min(), dataframe['Age'].max() + 1))
                    ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
                    ax.grid(False)
                    
                    st.pyplot(fig)
                else:
                    # Display error if 'Age' column has non-integer values
                    st.error('Age column contains other values than integers', icon="🚨")
            else:
                # Display error if 'Name' column has non-string values
                st.error('Name column contains other values than characters', icon="🚨")
        else:
            # Display error if the required columns are missing
            st.error('The uploaded file does not have the required columns: Name and Age', icon="🚨")
    else:
        # Display error if the uploaded file is not a CSV
        st.error('Please upload a file with a .csv extension', icon="🚨")
