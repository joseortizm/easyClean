#hello datasets
import pandas as pd
import os



def delete(df, cols):
    cols_to_drop = [col for col in df.columns if col not in cols]
    df = df.drop(cols_to_drop, axis='columns')
    return df

def join(paths, headers):
    n = len(paths)
    dataframes = []
    for i, dataset in enumerate(paths):
        if isinstance(dataset, pd.DataFrame):
            name_col = dataset.columns.tolist()
            column_name_mapping = {name: new_name for name, new_name in zip(name_col, headers)}
            dataset = dataset.rename(columns=column_name_mapping)
            dataframes.append(dataset)
        elif os.path.isfile(dataset):
            dataset = pd.read_csv(dataset)
            name_col = dataset.columns.tolist()
            if name_col != headers:
                column_name_mapping = {name: new_name for name, new_name in zip(name_col, headers)}
                dataset = dataset.rename(columns=column_name_mapping)
            dataframes.append(dataset)
        else:
            print('undetected element with index:', i)

    allData = dataframes[0]
    for df in dataframes[1:]:
        allData = pd.concat([allData, df])
        allData.reset_index(inplace=True, drop=True) 
    return allData 







