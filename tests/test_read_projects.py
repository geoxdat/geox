from geox import GeoX
from geox.exceptions import APIKeyException 
import pytest

from .dummy_data import API_KEY, PROJECT_VERSON_HASH, PROJECT_ID

@pytest.mark.parametrize('api_key, is_projects_loaded', [
    [API_KEY, True],
    ['wrong api key', False],
    [None, False],
    ])
def test_read_projects(api_key: str, is_projects_loaded: bool):
    try:
        geox = GeoX(api_key=api_key)
        projects = geox.read_all_projects()
        assert (projects is not None) == is_projects_loaded
        assert (geox.projects is not None) == is_projects_loaded
    
    except APIKeyException:
        assert True
    
    except Exception as e:
        print('Unhandled exceptions: ', e)
        assert False