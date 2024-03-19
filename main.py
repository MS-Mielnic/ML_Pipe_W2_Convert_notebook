from load_data import loader
from clean_data import clean_data
from visualize import create_graph

if __name__=="__main__":
    data = loader()
    new_df_legend, data_clean = clean_data(data)
    viz=create_graph(new_df_legend,data_clean)