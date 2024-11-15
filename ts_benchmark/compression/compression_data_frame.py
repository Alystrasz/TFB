import pandas as pd
from fast_linear_interpolation import FastLinearInterpolation


class CompressionDataFrame(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        super(CompressionDataFrame,  self).__init__(*args, **kwargs)
        self.fli = FastLinearInterpolation()

    @property
    def _constructor(self):
        return CompressionDataFrame

    def len(self):
        return len(self)

    @staticmethod
    def read_csv(path):
        return CompressionDataFrame(pd.read_csv(path))

#---- self test code
if __name__ == "__main__":
    compressed_series = CompressionDataFrame.read_csv('dataset/forecasting/PEMS-BAY.csv')
    print(f"Compressed series length: {compressed_series.len()}")
