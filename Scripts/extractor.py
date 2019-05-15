"""Accepts a target market and source folder, returns a csv of odds."""

import bz2
import json
import datetime
import os
import pandas as pd


def extract_data(market, folder):
    """Extract specific data for the specified market."""
    of_intrst = pd.read_csv('Output\\file_index.csv', header=0,
                            encoding='latin_1')

    of_intrst.columns = ["Filename", "EventId", "EventName", "CountryCode",
                         "MarketType", "Market",
                         "MarketTime", "SettledTime"]

    df_int = of_intrst[of_intrst['Market'] == market]
    df_int.reset_index(drop=True, inplace=True)

    print(df_int.head(), df_int.tail())

    files_intrst = df_int['Filename']

    path = os.getcwd()+'\\'+folder

    itera = 1
    errors = []
    all_together = []
    selectionIDs = [5851483, 1221386, 47973, 1222345,
                    1222346, 1485568, 2542449, 1485573]

    for file in files_intrst:

        with bz2.open(path+"\\"+file, 'r') as f2:
            data = f2.read().decode('utf-8')

        dict_list = [d.strip() for d in data.splitlines()]
        data = [json.loads(i) for i in dict_list]

        date = data[-1]['mc'][0]['marketDefinition']['openDate']
        kick_off = kick_off = int(1000*(datetime.datetime.strptime(date,
                                                                   "%Y-%m-%dT%H:%M:%S.%fZ") - datetime.datetime(1970, 1, 1)).total_seconds())

        eventName = data[0]['mc'][0]['marketDefinition']['eventName']
        eventID = data[0]['mc'][0]['marketDefinition']['eventId']

        print(data[0]['mc'][0]['marketDefinition']['eventName'],
              " : ", data[0]['mc'][0]['marketDefinition']['eventId'])

        time_ms = []
        batl = []
        ltp = []

        try:
            for dictionary in data:

                if 'rc' in dictionary['mc'][0] and 'batl' in dictionary['mc'][0]['rc'][0] and dictionary['mc'][0]['rc'][0]['id'] in selectionIDs and dictionary.get('pt') < kick_off:

                    time_ms.append(dictionary.get('pt'))
                    batl.append(dictionary['mc'][0]['rc'][0].get('batl')[0][1])
                    ltp.append(dictionary['mc'][0]['rc'][0].get('ltp'))

            ex_df = pd.DataFrame(zip(time_ms, batl, ltp))
            ex_df.columns = ['Time', 'BATL', 'LTP']
            one_hour = kick_off-3600000
            ex_df = ex_df[ex_df['Time'] > one_hour]
            hour_batl = ex_df['BATL'].median()
            hour_ltp = ex_df['LTP'].median()

            all_together.append([file, eventID, eventName, batl[-1], hour_batl,
                                 ltp[-1], hour_ltp])

            print(file, ' : ', itera)
            itera += 1

        except Exception as err:
            errors.append([file, err])
            print("An error has occured in filename: ", file)
            print(err)
            itera += 1
            pass

    together_df = pd.DataFrame(all_together)
    together_df.columns = ['Filename', 'EventID', 'Game', 'BATL at KO',
                           'One Hour BATL', 'LTP at KO', 'One Hour LTP']

    print(together_df.head())
    together_df.to_csv('Output.csv', index=False)

    errors = pd.DataFrame(errors)
    errors.to_csv('Errors.csv', index=False)

    print("Number of errors: ", len(errors))
