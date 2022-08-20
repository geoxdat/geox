from geox.connection import connect_to_endpoint
from geox.entity.api_endpoint import APIEndpoint
from geox.entity.dataset_type import DatasetType
from geox.http_response.http_dataset import HttpReponseDataset


def get_endpoint(dataset_type: str) -> str:
    '''get endpoint using dataset type'''
    if dataset_type == DatasetType.COLLAR:
        return APIEndpoint.GET_COLLAR_DATA
    
    elif dataset_type == DatasetType.SURVEY:
        return APIEndpoint.GET_SURVEY_DATA
    
    elif dataset_type == DatasetType.ALTERATION:
        return APIEndpoint.GET_ALTERATION_DATA
    
    elif dataset_type == DatasetType.ASSAY:
        return APIEndpoint.GET_ASSAY_DATA
    
    elif dataset_type == DatasetType.LITHO:
        return APIEndpoint.GET_LITHO_DATA
    
    elif dataset_type == DatasetType.MINERALISATION:
        return APIEndpoint.GET_MINERALISATION_DATA
    

def get_dataset_data(api_key: str, hash: str, next_index: int, dataset_type: str) -> HttpReponseDataset:
    response = connect_to_endpoint(
        url=get_endpoint(dataset_type),
        method='GET',
        headers={
            "api-key": api_key,
        },
        params={
            'hash': hash,
            'next_index': next_index,
        }
    )
    
    return HttpReponseDataset(response, dataset_type)
    
    