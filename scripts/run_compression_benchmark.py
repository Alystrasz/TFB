# -*- coding: utf-8 -*-
import os
import sys
import math
import numpy as np
import pandas as pd
import statistics

# Framework imports dark magic
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from ts_benchmark.common.constant import CONFIG_PATH, THIRD_PARTY_PATH
from ts_benchmark.pipeline import pipeline
from ts_benchmark.utils.parallel import ParallelBackend
sys.path.insert(0, THIRD_PARTY_PATH)
from ts_benchmark.compression.compression_data_frame import CompressionDataFrame

def diff(data1: pd.DataFrame, data2: pd.DataFrame, col: str, err: float):
    data1_values = data1[col]
    data2_values = data2[col]
    errors = []
    serrors = []
    
    for index, v in enumerate(data1_values):
        errors.append(abs(v - data2_values[index]))
        serrors.append(pow(v - data2_values[index], 2))
    mae = statistics.fmean(errors)
    mse = statistics.fmean(serrors)
    rmse = math.sqrt(mse)
    
    return f"{{\"error\": {err}, \"mae\": {mae}, \"mse\": {mse}, \"rmse\": {rmse}}}"

if __name__ == "__main__":
    series = pd.read_csv('dataset/forecasting/PEMS-BAY.csv')
    cols = np.sort(list(set(series['cols']))) # unique attributes
    col = 'channel_400002'

    # filter out the series of one column only
    series = pd.DataFrame(series.loc[series['cols'] == col])
    compressed_series = CompressionDataFrame(series.loc[series['cols'] == col])

    for factor in [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]:
        err = 0.1 * factor
        compressed_series = CompressionDataFrame(series.loc[series['cols'] == col])
        compressed_series.compress_test(err)
        print(diff(series, compressed_series, 'data', err))