import pandas as pd
import ciso8601
from datetime import datetime
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

    def compress(self, tolerated_error):
        print(self.head())

        data = [(datetime.timestamp(ciso8601.parse_datetime(t)), v) for t, v in zip(self['date'], self['data'])]
        self.fli.setError(tolerated_error)
        for d in data:
            try:
                self.fli.add(d[0], d[1])
            except:
                # todo: fix
                print(f"todo: fix failing add for {d}")

        # reattribute values
        assert self.len() == len(data)
        self['data'] = [self.fli.read(d[0]) for d in data]
        print(self.head())

#---- self test code
if __name__ == "__main__":
    compressed_series = CompressionDataFrame.read_csv('dataset/forecasting/PEMS-BAY.csv')
    print(f"Compressed series length: {compressed_series.len()}")

    # Compress with tolerated error
    error = 0.5
    compressed_series.compress(error)
