"""
This files selects the columns that will be needed to 
visualize the data and transforms the dataframe.
it returns a list of legends and clean df
"""
import pandas as pd
import altair as atl
from IPython import display


def cleaner(newdf):
    icons=['🟩','🟧','🟥','🟧','❓','🪵','🎚️']
    # check if the 'legend' column contains any of the icons we are interested in
    mask = newdf['LEGEND'].isin(icons)
    #select the data accoring our mask
    new_df_legend=newdf[mask].reset_index(drop=True)
    new_df_legend.dropna(axis=1, inplace=True)
    new_df_legend.columns=['value','keys']
    #size of new df
    new_size=new_df_legend.shape
    new_df_x=newdf.iloc[6:]
    new_df_x.columns = new_df_x.iloc[0]
    new_df_x = new_df_x[1:]
    new_df_x.reset_index(drop=True, inplace=True)
    new_df_x.ffill(inplace=True)
    new_df_x.dropna(axis=1,inplace=True)
    #list of sub categories
    columns_sub=new_df_x['Sub-Category'].unique()
    columns=list(new_df_x.columns)
    columns=columns[2:]
    categories=new_df_x['Telemetry Feature Category'].unique()
    dft=new_df_x.melt(id_vars=['Telemetry Feature Category',
                               'Sub-Category'], value_vars=columns)
    dft.rename(columns={6:'product'}, inplace=True)
    return new_df_legend, dft
