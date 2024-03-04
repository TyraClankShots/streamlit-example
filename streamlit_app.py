import altair as alt
import numpy as np
import pandas as pd
import pandas as pd
import streamlit as st
import requests 


# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import requests

# Set page title
st.set_page_config(page_title='Bradenton News Outlet')

# Define function to fetch data from API
def get_news():
    # API endpoint for Bradenton news
    url = 'https://myapi.com/bradenton-news'
    # Make GET request
    response = requests.get(url)
    # Convert response to json
    data = response.json()
    # Store data in dataframe
    df = pd.DataFrame(data['articles'])
    # Convert date column to datetime format
    df['publishedAt'] = pd.to_datetime(df['publishedAt'])
    # Sort dataframe by date
    df = df.sort_values(by='publishedAt', ascending=False)
    # Return dataframe
    return df

# Get data from API
df = get_news()

# Create sidebar with options for user
st.sidebar.header('Filter News by Category')
# Create checkbox for user to select categories
categories = st.sidebar.multiselect('Select Categories', list(df['category'].unique()))

# Filter dataframe based on user's selection
filtered_df = df[df['category'].isin(categories)]

# Display filtered dataframe in a table
