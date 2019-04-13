"""Function to return a dict of filename and market for files in 'Data'."""

import bz2
import json
# import datetime
# import glob
# import pandas as pd
# import numpy as np
import os
# from os import listdir
# from os.path import isfile, join


def data_indexer():
    """Create and index of filenames and markets from files in 'Data'."""
    path = os.getcwd()+'\\Test_Data'
    index_list = []

    for file in os.listdir(path):
        with bz2.open(path+"\\"+file, 'r') as f:
            data = f.read().decode('utf-8')
        dict_list = [d.strip() for d in data.splitlines()]
        data = [json.loads(i) for i in dict_list]

        id = data[-1]['mc'][0]['id']
        eventId = data[-1]['mc'][0]['marketDefinition']['eventId']
        eventName = data[-1]['mc'][0]['marketDefinition']['eventName']
        openDate = data[-1]['mc'][0]['marketDefinition']['openDate']

        index_list.append([id, eventId, eventName, openDate])

    print(index_list)
