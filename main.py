"""Main function platform, all scripts should be called from here."""

# from Scripts.file_indexer import file_list
# from Scripts.display_markets import display_markets
from Scripts.extractor import extract_data
import shutil


markets = ['Over/Under 0.5 Goals', 'Over/Under 1.5 Goals',
           'Over/Under 2.5 Goals', 'Over/Under 3.5 Goals',
           'Over/Under 4.5 Goals', 'Over/Under 5.5 Goals',
           'Over/Under 6.5 Goals', 'Over/Under 7.5 Goals']

names = ['0_5', '1_5', '2_5', '3_5', '4_5', '5_5', '6_5', '7_5']

for i in range(len(markets)):
    extract_data(markets[i], 'Data')
    shutil.move('Output.csv', 'Over_Under Output/'+names[i]+'.csv')
    shutil.move('Error.csv', 'Over_Under Output/'+names[i]+'_errors.csv')
