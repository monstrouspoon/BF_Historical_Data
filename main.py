"""Main function platform, all scripts should be called from here."""

from Scripts.file_indexer import file_list
from Scripts.display_markets import display_markets
from Scripts.extractor import extract_data

"""file_list() is specifically for creating an index of all files in "Data".
    It requires about an hour per gigabyte of data."""
file_list('Data', 100)

""" Print out the most popular markets"""
# display_markets(5)

"""Extract data from a specific markets to .csv"""
# extract_data('Over/Under 0.5 Goals', 'Data')
