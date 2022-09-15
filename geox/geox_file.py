import pandas as pd


class GeoXFile:
    def __init__(self, version_hash: str, dataframe: pd.DataFrame):
        self.version_hash = version_hash
        self.dataframe = dataframe
        