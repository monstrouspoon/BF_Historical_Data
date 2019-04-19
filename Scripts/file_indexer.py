"""Function to return a dict of filename and market for files in 'Data'."""

import bz2
import json
import pandas as pd
import os
import sys


def file_list(folder, chunk_size):
    """Create and index of filenames and markets from files in 'Data'."""
    output_exists = os.path.isfile('Output\\output.csv')
    if output_exists is True:
        print("+++++++++++++++++++++++++++++++++")
        print("  OUTPUT FILE ALREADY EXISTS     ")
        print(" DELETE OUTPUT FILE TO CONTINUE  ")
        print("+++++++++++++++++++++++++++++++++")
        sys.exit()

    path = os.getcwd()+'\\'+folder
    file_list = os.listdir(path)
    file_itr = iter(file_list)
    columns = ['Filename', 'Event ID', 'Game', 'Country Code', 'Market',
               'Market Name', 'Market Time', 'Settlement Time']

    index_list = []
    chunk_no = 1

    for i in range(len(file_list)):
        file = next(file_itr)
        with bz2.open(path+"\\"+file, 'r') as f:
            data = f.read().decode('utf-8')
        dict_list = [d.strip() for d in data.splitlines()]
        data = [json.loads(i) for i in dict_list]

        eventId = data[-1]['mc'][0]['marketDefinition']['eventId']
        eventName = data[-1]['mc'][0]['marketDefinition']['eventName']
        countryCode = data[-1]['mc'][0]['marketDefinition']['countryCode']

        marketType = data[-1]['mc'][0]['marketDefinition']['marketType']
        name = data[-1]['mc'][0]['marketDefinition']['name']

        marketTime = data[-1]['mc'][0]['marketDefinition']['marketTime']
        settledTime = data[-1]['mc'][0]['marketDefinition']['settledTime']

        if i % chunk_size == 0 and i > 0:
            index_list.append([file, eventId, eventName, countryCode,
                               marketType, name,
                               marketTime, settledTime])

            temp_df = pd.DataFrame(index_list)
            with open('Output\\output.csv', 'a', newline='') as f:
                temp_df.to_csv(f, header=False, index=False)

            index_list = []
            print("Chunk number ", chunk_no, " finished: ",
                  round(((chunk_no*chunk_size)/len(file_list))*100, 2),
                  "% completed.")
            chunk_no += 1

        else:
            # print(file)
            index_list.append([file, eventId, eventName, countryCode,
                               marketType, name,
                               marketTime, settledTime])

    temp_df = pd.DataFrame(index_list)
    with open('Output\\output.csv', 'a', newline='') as f:
        temp_df.to_csv(f, header=False, index=False)

    df = pd.read_csv('Output\\output.csv', index_col=None, names=columns)
    df.to_csv('Output\\output.csv', index=False)
    print('Done')
