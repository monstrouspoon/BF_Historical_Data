"""Function to return a dict of filename and market for files in 'Data'."""

import bz2
import json
import pandas as pd
import os


def file_indexer():
    """Create and index of filenames and markets from files in 'Data'."""
    path = os.getcwd()+'\\Data'
    index_list = []
    itera = 1

    for file in os.listdir(path):
        with bz2.open(path+"\\"+file, 'r') as f:
            data = f.read().decode('utf-8')
        dict_list = [d.strip() for d in data.splitlines()]
        data = [json.loads(i) for i in dict_list]

        id = data[-1]['mc'][0]['id']
        eventId = data[-1]['mc'][0]['marketDefinition']['eventId']
        eventName = data[-1]['mc'][0]['marketDefinition']['eventName']
        countryCode = data[-1]['mc'][0]['marketDefinition']['countryCode']

        marketType = data[-1]['mc'][0]['marketDefinition']['marketType']
        name = data[-1]['mc'][0]['marketDefinition']['name']

        openDate = data[-1]['mc'][0]['marketDefinition']['openDate']
        marketTime = data[-1]['mc'][0]['marketDefinition']['marketTime']
        settledTime = data[-1]['mc'][0]['marketDefinition']['settledTime']

        index_list.append([id, eventId, eventName, countryCode,
                           marketType, name,
                           openDate, marketTime, settledTime])
        print(round((itera/len(os.listdir(path)))*100, 1), "%")
        itera += 1

    columns = ['Filename', 'Event ID', 'Game', 'Country Code', 'Market',
               'Market Name', 'Open Date', 'Market Time', 'Settlement Time']

    index_df = pd.DataFrame(index_list, columns=columns)
    index_df.to_csv('Output\\File_index.csv', index=False)
