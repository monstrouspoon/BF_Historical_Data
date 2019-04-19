# BF_Historical_Data
Tools for the exploration of BF historical data archives, and for finding and extracting specific data of interest.

Specifically this project is meant to provide a means of sorting through the archived data, provided initially as a .tar archive containing .bz2 archives related to individual markets.  Inside each .bz2 is an file without a file extension which needs to be read in and then parsed as a json file.  

The dictionaries within are then sorted through to find relevant information which can be exported to a spreadsheet for laymen to play with, though the intention is that most of that type of work can be done using python scripts.

Functions are required to do the following:
    1. Create a quick-to-access index of file names and the information within.
    2. Extract data from files of interest and generate statistical summaries
    3. Make use of this information in whatever model is required.
