import json
import dill
import os
import pandas as pd

from datetime import datetime


def predict():
    path = os.path.expanduser('~/airflow_hw')
    model = os.listdir(f'{path}/data/models')[0]
    test_files = os.listdir(f'{path}/data/test')
    csv_filename = f'{path}/data/predictions/preds_{datetime.now().strftime("%Y%m%d%H%M")}.csv'
    with open(f'{path}/data/models/{model}', 'rb') as file:
        model = dill.load(file)
    data = []
    for file in test_files:
        with open(f'{path}/data/test/{file}') as js:
            line = pd.DataFrame.from_dict([json.load(js)])
            data.append([line["id"][0], model.predict(line)[0]])
    df = pd.DataFrame(data, columns=['car_id', 'pred'])
    df.to_csv(csv_filename)
    print(df)


if __name__ == '__main__':
    predict()
