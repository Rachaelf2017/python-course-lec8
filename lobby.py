import pandas as pd
import numpy as np
from pandas import DataFrame, Series
import sys


def csv_reader(path):
    df =  pd.read_csv(path)
    df[['COMPENSATION']] = df[['COMPENSATION']].replace('[\$,]','',regex=True).astype(float)

    frame = df['COMPENSATION']
    return frame



csv_reader(sys.argv[1])


# df[['Currency']] = df[['Currency']].replace('[\$,]','',regex=True).astype(float)

frame = csv_reader(sys.argv[1])
# grouped = frame['CLIENT'].groupby(frame['COMPENSATION']) - wrong
grouped = frame.groupby(frame['CLIENTS'])['COMPENSATION']
print group
