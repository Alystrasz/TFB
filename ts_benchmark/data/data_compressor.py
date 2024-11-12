import pandas as pd

class DataCompressor():
    def __init__(self):
        pass

    def regular_removal(self, df: pd.DataFrame, modulo: int) -> pd.DataFrame:
        data = df.copy()
        data['index'] = range(0, len(data))
        data = data[data['index'] % modulo != 0]
        data = data.drop(['index'], axis=1)
        return data