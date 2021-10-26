import seaborn as sns
import pandas as pd

def bPlotter1(df):
    #na_min([], default="EMPTY")
    df = df.loc[:, (df.isna().sum(axis=0) > 0)]
    df = df.select_dtypes(exclude="object")
    ax = sns.barplot(data=df)
    
    return ax