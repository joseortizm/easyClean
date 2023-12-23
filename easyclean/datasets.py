#hello datasets
import pandas as pd
import os



def delete(df, cols):
    cols_to_drop = [col for col in df.columns if col not in cols]
    df = df.drop(cols_to_drop, axis='columns')
    return df

def join(paths):
    n = len(paths)
    dataframes = []
    for i, dataset in enumerate(paths):
        if isinstance(dataset, pd.DataFrame):
            #print('dataframe')
            dataframes.append(dataset)
        elif os.path.isfile(dataset):
            #print('es archivo')
            df = pd.read_csv(dataset)
            dataframes.append(df)
        else:
            print('undetected element with index:', i)

    allData = dataframes[0]
    for df in dataframes[1:]:
        allData = pd.concat([allData, df])
    return allData 







