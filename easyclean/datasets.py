#hello datasets
import pandas as pd



def delete(df, cols):
    cols_to_drop = [col for col in df.columns if col not in cols]
    df = df.drop(cols_to_drop, axis='columns')
    return df

def join(paths):
    n = len(paths)
    for i in paths:
        df = pd.read_csv(i)
        if  isinstance(df.columns[0], str):
            print('header')
            print(df.columns[1])
        else:
            print('no header')

        _, col = df.shape
        #print(col)         
    #return n







