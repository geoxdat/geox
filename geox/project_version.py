from datetime import datetime
from geox.api_caller.get_dataset import get_dataset_data
from geox.entity.dataset_type import DatasetType
from geox.http_response.http_dataset import HttpReponseDataset
from tqdm import tqdm
from typing import Optional, Tuple
import os
import pandas as pd
import numpy as np


class ProjectVersion:
    """Project version defined by project version hash, 
    may contain collar, survey, alteration, assay, litho, or mineralisation dataset.
    """
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
        
        self.num_of_survey_rows: int = None
        self.num_of_collar_rows: int = None
        self.num_of_alteration_rows: int = None
        self.num_of_assay_rows: int = None
        self.num_of_litho_rows: int = None
        self.num_of_mineralisation_rows: int = None
        
        # private variables
        self._api_key: str = None
        self._is_updated: bool = False
        self._timestamp = datetime.now()
        self._default_filetype = '.geox'
    
    
    def set_api_key(self, api_key: str) -> None:
        self._api_key = api_key
        
        
    def read_collar_data(self, filename: str=DatasetType.COLLAR, save_to_file: bool=True) -> pd.DataFrame:
        """read collar dataset from server

        Args:
            filename (str, optional): output filename. Defaults to DatasetType.COLLAR.
            save_to_file (bool, optional): is save to a file. Defaults to True.

        Returns:
            pd.DataFrame: dataset pandas dataframe
        """
        if self.num_of_collar_rows == 0:
            print('No collar data in this dataset')
            return None
        
        bar = tqdm(desc='Collar Dataset', total=self.num_of_collar_rows)
        df, next_index = self._read_initial_dataframe(filename)
        if df is not None: bar.update(df.shape[0])
        self.collar = self._read_dataset_data(
            df, 
            next_index, 
            self._create_full_filename(filename), 
            save_to_file, 
            DatasetType.COLLAR,
            bar,
            )
        return self.collar

        
    def read_survey_data(self, filename: str=DatasetType.SURVEY, save_to_file: bool=True) -> pd.DataFrame:
        """read survey dataset from server

        Args:
            filename (str, optional): output filename. Defaults to DatasetType.SURVEY.
            save_to_file (bool, optional): is save to a file. Defaults to True.

        Returns:
            pd.DataFrame: dataset pandas dataframe
        """
        if self.num_of_survey_rows == 0:
            print('No survey data in this dataset')
            return None
        
        bar = tqdm(desc='Survey Dataset', total=self.num_of_survey_rows)
        df, next_index = self._read_initial_dataframe(filename)
        if df is not None: bar.update(df.shape[0])
        self.survey = self._read_dataset_data(
            df, 
            next_index, 
            self._create_full_filename(filename), 
            save_to_file, 
            DatasetType.SURVEY,
            bar,
            )
        return self.survey

        
    def read_alteration_data(self, filename: str=DatasetType.ALTERATION, save_to_file: bool=True) -> pd.DataFrame:
        """read alteration dataset from server

        Args:
            filename (str, optional): output filename. Defaults to DatasetType.ALTERATION.
            save_to_file (bool, optional): is save to a file. Defaults to True.

        Returns:
            pd.DataFrame: dataset pandas dataframe
        """
        if self.num_of_alteration_rows == 0:
            print('No alteration data in this dataset')
            return None
        
        bar = tqdm(desc='Alteration Dataset', total=self.num_of_alteration_rows)
        df, next_index = self._read_initial_dataframe(filename)
        if df is not None: bar.update(df.shape[0])
        self.alteration = self._read_dataset_data(
            df, 
            next_index, 
            self._create_full_filename(filename), 
            save_to_file, 
            DatasetType.ALTERATION,
            bar,
            )
        return self.alteration

        
    def read_assay_data(self, filename: str=DatasetType.ASSAY, save_to_file: bool=True) -> pd.DataFrame:
        """read assay dataset from server

        Args:
            filename (str, optional): output filename. Defaults to DatasetType.ASSAY.
            save_to_file (bool, optional): is save to a file. Defaults to True.

        Returns:
            pd.DataFrame: dataset pandas dataframe
        """
        if self.num_of_assay_rows == 0:
            print('No assay data in this dataset')
            return None
        
        bar = tqdm(desc='Assay Dataset', total=self.num_of_assay_rows)
        df, next_index = self._read_initial_dataframe(filename)
        if df is not None: bar.update(df.shape[0])
        self.assay = self._read_dataset_data(
            df, 
            next_index, 
            self._create_full_filename(filename), 
            save_to_file, 
            DatasetType.ASSAY,
            bar,
            )
        return self.assay

        
    def read_litho_data(self, filename: str=DatasetType.LITHO, save_to_file: bool=True) -> pd.DataFrame:
        """read litho dataset from server

        Args:
            filename (str, optional): output filename. Defaults to DatasetType.LITHO.
            save_to_file (bool, optional): is save to a file. Defaults to True.

        Returns:
            pd.DataFrame: dataset pandas dataframe
        """
        if self.num_of_litho_rows == 0:
            print('No litho data in this dataset')
            return None
        
        bar = tqdm(desc='Litho Dataset', total=self.num_of_litho_rows)
        df, next_index = self._read_initial_dataframe(filename)
        if df is not None: bar.update(df.shape[0])
        self.litho = self._read_dataset_data(
            df, 
            next_index, 
            self._create_full_filename(filename), 
            save_to_file, 
            DatasetType.LITHO,
            bar,
            )
        return self.litho

        
    def read_mineralisation_data(self, filename: str=DatasetType.MINERALISATION, save_to_file: bool=True) -> pd.DataFrame:
        """read mineralisation dataset from server

        Args:
            filename (str, optional): output filename. Defaults to DatasetType.MINERALISATION.
            save_to_file (bool, optional): is save to a file. Defaults to True.

        Returns:
            pd.DataFrame: dataset pandas dataframe
        """
        if self.num_of_mineralisation_rows == 0:
            print('No mineralisation data in this dataset')
            return None
        
        bar = tqdm(desc='Mineralisation Dataset', total=self.num_of_mineralisation_rows)
        df, next_index = self._read_initial_dataframe(filename)
        if df is not None: bar.update(df.shape[0])
        self.mineralisation = self._read_dataset_data(
            df, 
            next_index, 
            self._create_full_filename(filename), 
            save_to_file, 
            DatasetType.MINERALISATION,
            bar,
            )
        return self.mineralisation


    def _create_full_filename(self, filename: str) -> str:
        '''Creating full filename with file format'''
        return filename + self._default_filetype
    
    
    def _read_initial_dataframe(self, filename: str) -> Tuple[pd.DataFrame, int]:
        '''read or create initial dataframe'''
        full_filename = self._create_full_filename(filename)
        df = pd.read_pickle(full_filename) if os.path.isfile(full_filename) else None
        next_index = df['id'].max() + 1 if os.path.isfile(full_filename) else -1
        return df, next_index


    def _read_dataset_data(
        self, 
        df: pd.DataFrame, 
        next_index: int, 
        full_filename: str, 
        save_to_file: bool, 
        dataset_type: str,
        progress_bar: tqdm,
        ) -> pd.DataFrame:
        '''read dataset data, call api and loop if there is data on the next index, save dataframe to file on each loop'''
        while next_index > -2:
            http_response = get_dataset_data(self._api_key, self.hash, next_index, dataset_type)
            next_index = http_response.get_next_index()
            
            # creating dataframe
            new_df = self._build_dataframe(df, http_response)
            if new_df is not None: 
                df = new_df  
            else:
                break
            
            # create pickle file
            if save_to_file: df.to_pickle(full_filename)
            progress_bar.update(len(http_response.data))
        
        return df
    
    
    def _build_dataframe(self, df: Optional[pd.DataFrame], http_response: HttpReponseDataset) -> Optional[pd.DataFrame]:
        '''create dataframe from http response, append the previous dataframe if exists'''
        # create dataframe
        if len(http_response.data) > 0:
            new_df = pd.DataFrame.from_dict(http_response.data)
            new_df = new_df.fillna(value=np.nan)
        else:
            return None
        
        # appending existed dataframe
        if df is not None:
            # df = df.append(new_df, ignore_index=True)
            df = pd.concat([df, new_df], ignore_index=True)
        else:
            df = new_df
            
        return df
    