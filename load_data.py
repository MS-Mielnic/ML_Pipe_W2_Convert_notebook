"""
this function reads from a google sheet that is posted 
in an existing github project. In this way if the file is
modified when you run the project you get the latest version
It returns a dataframe
"""
import pandas as pd

def loader():
    """
    receives constants  specific to this file
    in github to read a csv
    """
    sheet_id = '1ZMFrD6F6tvPtf_8McC-kWrNBBec_6Si3NW6AoWf3Kbg'
    sheet_name = 'xxdata'
    url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
    newdf = pd.read_csv(url)
    return newdf
