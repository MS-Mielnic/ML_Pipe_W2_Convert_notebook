"""
this function reads from a google sheet that is posted 
in an existing github project. In this way if the file is
modified when you run the project you get the latest version
It returns a dataframe
"""
import pandas as pd

def loader():
    SHEET_ID = '1ZMFrD6F6tvPtf_8McC-kWrNBBec_6Si3NW6AoWf3Kbg'
    SHEET_NAME = 'xxdata'
    url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
    newdf = pd.read_csv(url)
    return newdf