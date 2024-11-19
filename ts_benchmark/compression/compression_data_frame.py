import pandas as pd
import ciso8601
from datetime import datetime
from ts_benchmark.compression.fast_linear_interpolation import FastLinearInterpolation


class CompressionDataFrame(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        super(CompressionDataFrame,  self).__init__(*args, **kwargs)
        self.fli = FastLinearInterpolation()
        self.models = {}

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

        timestamps = [datetime.timestamp(ciso8601.parse_datetime(str(t))) for t in self.index]
        for value in self.columns.values:
            model = FastLinearInterpolation()
            model.setError(tolerated_error)
            for index, r in enumerate(self[value]):
                try:
                    model.add(timestamps[index], r)
                except:
                    # todo: fix
                    print(f"todo: fix failing add for [{value}]{index, r}")
            self.models[value] = model
            print(f"=> Column {value} stored in FLI model.")
        print("Model conversion done.")

        # reattribute values
        for value in self.columns.values:
            self[value] = [self.models[value].read(t) for t in timestamps]
        print(self.head())

    def compress_test(self, tolerated_error):
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
    compressed_series.compress_test(error)
