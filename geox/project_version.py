from datetime import datetime
from typing import Optional, Tuple
import os
import pickle

from tqdm import tqdm
import numpy as np
import pandas as pd

from geox.api_caller.get_dataset import get_dataset_data
from geox.entity.dataset_type import DatasetType
from geox.exceptions import DatasetTypeException
from geox.geox_file import GeoXFile
from geox.http_response.http_dataset import HttpReponseDataset


class ProjectVersion:
    """Project version defined by project version hash, 
    may contain collar, survey, alteration, assay, litho, or mineralisation dataset.
    """
    def __init__(self, hash: str):
        self.hash: str = hash
        
        self.id: int = None
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
        data = self._read_dataset_data(
            dataset_type=DatasetType.COLLAR, 
            filename=filename, 
            save_to_file=save_to_file
            )
        return data

        
    def read_survey_data(self, filename: str=DatasetType.SURVEY, save_to_file: bool=True) -> pd.DataFrame:
        """read survey dataset from server

        Args:
            filename (str, optional): output filename. Defaults to DatasetType.SURVEY.
            save_to_file (bool, optional): is save to a file. Defaults to True.

        Returns:
            pd.DataFrame: dataset pandas dataframe
        """
        data = self._read_dataset_data(
            dataset_type=DatasetType.SURVEY, 
            filename=filename, 
            save_to_file=save_to_file
            )
        return data

        
    def read_alteration_data(self, filename: str=DatasetType.ALTERATION, save_to_file: bool=True) -> pd.DataFrame:
        """read alteration dataset from server

        Args:
            filename (str, optional): output filename. Defaults to DatasetType.ALTERATION.
            save_to_file (bool, optional): is save to a file. Defaults to True.

        Returns:
            pd.DataFrame: dataset pandas dataframe
        """
        data = self._read_dataset_data(
            dataset_type=DatasetType.ALTERATION, 
            filename=filename, 
            save_to_file=save_to_file
            )
        return data

        
    def read_assay_data(self, filename: str=DatasetType.ASSAY, save_to_file: bool=True) -> pd.DataFrame:
        """read assay dataset from server

        Args:
            filename (str, optional): output filename. Defaults to DatasetType.ASSAY.
            save_to_file (bool, optional): is save to a file. Defaults to True.

        Returns:
            pd.DataFrame: dataset pandas dataframe
        """
        data = self._read_dataset_data(
            dataset_type=DatasetType.ASSAY, 
            filename=filename, 
            save_to_file=save_to_file
            )
        return data
  
        
    def read_litho_data(self, filename: str=DatasetType.LITHO, save_to_file: bool=True) -> pd.DataFrame:
        """read litho dataset from server

        Args:
            filename (str, optional): output filename. Defaults to DatasetType.LITHO.
            save_to_file (bool, optional): is save to a file. Defaults to True.

        Returns:
            pd.DataFrame: dataset pandas dataframe
        """
        data = self._read_dataset_data(
            dataset_type=DatasetType.LITHO, 
            filename=filename, 
            save_to_file=save_to_file
            )
        return data

        
    def read_mineralisation_data(self, filename: str=DatasetType.MINERALISATION, save_to_file: bool=True) -> pd.DataFrame:
        """read mineralisation dataset from server

        Args:
            filename (str, optional): output filename. Defaults to DatasetType.MINERALISATION.
            save_to_file (bool, optional): is save to a file. Defaults to True.

        Returns:
            pd.DataFrame: dataset pandas dataframe
        """
        data = self._read_dataset_data(
            dataset_type=DatasetType.MINERALISATION, 
            filename=filename, 
            save_to_file=save_to_file
            )
        return data


    def _create_full_filename(self, filename: str) -> str:
        '''Creating full filename with file format'''
        return filename + self._default_filetype
    
    
    def _initialization(self, filename: str) -> Tuple[pd.DataFrame, int]:
        '''read or create initial dataframe'''
        df = self._read_saved_dataframe(filename)
        next_index = self._read_next_index(df)
        return df, next_index
   
    
    def _read_saved_dataframe(self, filename: str) -> pd.DataFrame:
        df = None
        full_filename = self._create_full_filename(filename)
        if os.path.isfile(full_filename):
            geox_file = self._read_from_GeoXFile(full_filename)
            if geox_file and geox_file.version_hash == self.hash:
                df = geox_file.dataframe
            
        return df


    def _read_next_index(self, df: pd.DataFrame) -> int:
        next_index = df['id'].max() + 1 if df is not None else -1
        return next_index


    def _get_number_of_rows(self, dataset_type: str):
        num = 0
        if dataset_type == DatasetType.COLLAR:
            num = self.num_of_collar_rows
        
        elif dataset_type == DatasetType.SURVEY:
            num = self.num_of_survey_rows
        
        elif dataset_type == DatasetType.ALTERATION:
            num = self.num_of_alteration_rows
        
        elif dataset_type == DatasetType.ASSAY:
            num = self.num_of_assay_rows
        
        elif dataset_type == DatasetType.LITHO:
            num = self.num_of_litho_rows
        
        elif dataset_type == DatasetType.MINERALISATION:
            num = self.num_of_mineralisation_rows
            
        else:
            raise DatasetTypeException(f"{dataset_type} is not a valid dataset type")
        
        return num
    

    def _read_dataset_data(self, dataset_type: str, filename: str, save_to_file: bool):
        data = None # iniitalize returned data as None
        
        # count num of row in the dataset
        num_of_rows = self._get_number_of_rows(dataset_type)
        if num_of_rows == 0:
            print(f'No {dataset_type} data in this dataset')
            return None
        
        # create progress bar
        bar = tqdm(desc=f'{dataset_type} dataset', total=num_of_rows)
        
        # check saved version
        if save_to_file:
            df, next_index = self._initialization(filename)
            if df is not None: bar.update(df.shape[0])
        else:
            df, next_index = None, -1
        
        # check is dataframe size is already same as number of rows
        if df is not None and df.shape[0] == num_of_rows:
            data = df
        else:
            # if not, call api to retrieve data
            data = self._execute_api(
                df=df, 
                next_index=next_index, 
                full_filename=self._create_full_filename(filename), 
                save_to_file=save_to_file, 
                dataset_type=dataset_type,
                progress_bar=bar,
                )
        return data

        
    def _execute_api(
        self, 
        df: pd.DataFrame, 
        next_index: int, 
        full_filename: str, 
        save_to_file: bool, 
        dataset_type: str,
        progress_bar: tqdm,
        ) -> pd.DataFrame:
        '''read dataset data, call api and loop if there is data on the next index, save dataframe to file on each loop'''
        while next_index >= -1:
            http_response = get_dataset_data(self._api_key, self.hash, next_index, dataset_type)
            next_index = http_response.get_next_index()
            
            # creating dataframe
            new_df = self._build_dataframe(df, http_response)
            if new_df is not None: 
                df = new_df  
            else:
                break
            
            # create pickle file
            if save_to_file: 
                self._save_to_GeoXFile(df, full_filename)
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
    
    
    def _read_from_GeoXFile(self, full_filename) -> GeoXFile:
        with open(full_filename, 'rb') as f:
            data = pickle.load(f)
            if isinstance(data, GeoXFile):
                return data
            else: 
                return None
    
    
    def _save_to_GeoXFile(self, data: pd.DataFrame, full_filename: str):
        with open(full_filename, 'wb') as file:
            data = GeoXFile(version_hash=self.hash, dataframe=data)
            pickle.dump(data, file)
            
            
    def __str__(self):
        return f"""Project Version {self.hash}
total survey rows : {self.num_of_survey_rows}
total collar rows : {self.num_of_collar_rows}
total alteration rows : {self.num_of_alteration_rows}
total assay rows : {self.num_of_assay_rows}
total litho rows : {self.num_of_litho_rows}
total mineralisation rows : {self.num_of_mineralisation_rows}
"""
