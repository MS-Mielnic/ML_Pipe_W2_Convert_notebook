"""
This script is from the comparing Edrs jupyter notebook
"""
from load_data import loader
from clean_data import cleaner
from visualize import create_graph

if __name__=="__main__":
    data = loader()
    new_df_legend, data_clean = cleaner(data)
    viz=create_graph(new_df_legend,data_clean)
    viz.save('table.html', inline=True)