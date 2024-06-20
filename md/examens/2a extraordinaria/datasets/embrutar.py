import random
import pandas as pd
import numpy as np

def add_nulls_random(dataframe,column,percentage):
    random_index = random.sample(range(0,len(dataframe)),int(len(dataframe)*percentage))
    dataframe.loc[random_index,column] = np.nan
    return dataframe

df = pd.read_csv("Laptop_price.csv")

add_nulls_random(df,"Brand",0.05)
add_nulls_random(df,"Processor_Speed",0.10)
add_nulls_random(df,"RAM_Size",0.15)
add_nulls_random(df,"Screen_Size",0.10)
add_nulls_random(df,"Weight",0.25)
add_nulls_random(df,"Price",0.05)

df.to_csv("Laptop_price_dirty.csv",index=False)