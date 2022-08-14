from datetime import datetime
import pandas as pd

from geox.entity.dataset_type import DatasetType

class   ProjectVersion:
    def __init__(self, hash: str):
        self.hash: str = hash
        
        self.id: int = None
        
        self.collar: pd.DataFrame = None
        self.survey: pd.DataFrame = None
        self.alteration: pd.DataFrame = None
        self.assay: pd.DataFrame = None
        self.litho: pd.DataFrame = None
        self.mineralisation: pd.DataFrame = None
        
        self.created_at: datetime = None
        
        self.num_of_collar_rows: int = None
        self.num_of_survey_rows: int = None
        self.num_of_alteration_rows: int = None
        self.num_of_assay_rows: int = None
        self.num_of_litho_rows: int = None
        self.num_of_mineralisation_rows: int = None
        
        # private variables
        self._is_updated: bool = False
        self._timestamp = datetime.now()
        
        
    def read_collar_data(self, filename: str=DatasetType.COLLAR, save_to_file: bool=True):
        ...

        
    def read_survey_data(self, filename: str=DatasetType.SURVEY, save_to_file: bool=True):
        ...

        
    def read_alteration_data(self, filename: str=DatasetType.ALTERATION, save_to_file: bool=True):
        ...

        
    def read_assay_data(self, filename: str=DatasetType.ASSAY, save_to_file: bool=True):
        ...

        
    def read_litho_data(self, filename: str=DatasetType.LITHO, save_to_file: bool=True):
        ...

        
    def read_mineralisation_data(self, filename: str=DatasetType.MINERALISATION, save_to_file: bool=True):
        ...

        
    