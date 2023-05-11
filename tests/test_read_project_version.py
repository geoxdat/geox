from geox import GeoX
from geox.exceptions import APIKeyException 
import pytest

from .dummy_data import API_KEY, PROJECT_VERSON_HASH, PROJECT_ID

@pytest.mark.parametrize('api_key, project_id, hash, is_projects_loaded', [
    [API_KEY, PROJECT_ID, PROJECT_VERSON_HASH, True],
    [API_KEY, PROJECT_ID, 'WRONG', False],
    [API_KEY, 'WRONG', PROJECT_VERSON_HASH, False],
    ['wrong api key', PROJECT_ID, PROJECT_VERSON_HASH, False],
    ['wrong api key', PROJECT_ID, 'WRONG', False],
    ['wrong api key', 'WRONG', 'WRONG', False],
    [None, None, None, False],
    ])
def test_read_project_version(api_key: str, project_id: str, hash: str, is_projects_loaded: bool):
    try:
        geox = GeoX(api_key=api_key)
        project = geox.read_project(project_id)
        if project:
            project_version = project.read_project_version(hash)
            assert (project_version is not None) == is_projects_loaded
        else:
            assert (project is not None) == is_projects_loaded
    
    except APIKeyException:
        assert True
    
    except Exception as e:
        print('Unhandled exceptions: ', e)
        assert False