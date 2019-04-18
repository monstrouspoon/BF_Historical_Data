import pandas as pd
"""Function for displaying the names of markets in file_index.csv"""


def display_markets(c=10):
    """Display the top c-number of most popular markets"""
    df = pd.read_csv('Output\\file_index.csv', encoding='latin-1')
    df = df['Market'].value_counts()
    df = df.reset_index()
    df.columns = ['Most Popular Markets', 'Count']
    print('Most popular markets:')
    print(df.iloc[0:c, 0])
