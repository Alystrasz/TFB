import pandas as pd

class DataCompressor():
    def __init__(self):
        pass

    def regular_removal(self, df: pd.DataFrame, modulo: int, linear_replace: bool = False) -> pd.DataFrame:
        """
        Compresses a time series by regularly removing values.

        :param df: Series to be compressed.
        :param modulo: All values matching `index % modulo == 0` will be updated.
        :param linear_replace: Whether data points should be removed, or replaced using interpolation between neighbouring values.
        :return: A compressed time series in DataFrame format.
        """
        
        data = df.copy()

        # This won't work with benchmarks expecting consistent data frequency
        if not linear_replace:
            data['index'] = range(0, len(data))
            data = data[data['index'] % modulo != 0]

            # Remove 'index' column not to fiddle with the benchmark
            data = data.drop(['index'], axis=1)

        else:
            # 1. find indexes whose values must be updated
            indexes = [x for x in range(len(data)) if x % modulo == 0]

            # 2. replace values at indexes using neighbouring values
            for i in indexes:
                if i == len(data)-1:
                    data.iloc[i, [0]] = [data.iloc[i-1, [0]]]
                else:
                    data.iloc[i, [0]] = [(data.iloc[i-1, [0]] + data.iloc[i+1, [0]]) / 2]

        return data