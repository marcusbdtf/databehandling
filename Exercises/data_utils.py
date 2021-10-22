import seaborn as sns
import pandas as pd
import 

def bPlotter1(df):
    df = df.loc[:, (df.isna().sum(axis=0) > min_na)]
    df = df.select_dtypes(exclude="object")
    ax = sns.barplot(data=df)
    
    return ax
bPlotter1(df)