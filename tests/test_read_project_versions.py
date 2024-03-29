from geox import GeoX
from geox.exceptions import APIKeyException 
import pytest
from .dummy_data import API_KEY, PROJECT_VERSON_HASH, PROJECT_ID


@pytest.mark.parametrize('api_key, project_id, is_projects_loaded', [
    [API_KEY, PROJECT_ID, True],
    [API_KEY, 'WRONG', False],
    ['wrong api key', PROJECT_ID, False],
    ['wrong api key', 'WRONG', False],
    [None, None, False],
    ])
def test_read_project_versions(api_key: str, project_id: str, is_projects_loaded: bool):
    try:
        geox = GeoX(api_key=api_key)
        project = geox.read_project(project_id)
        if project:
            project_versions = project.read_all_project_versions()
            assert (project_versions is not None) == is_projects_loaded
            assert (project.project_versions is not None) == is_projects_loaded
            
        else:
            assert (project is not None) == is_projects_loaded
    
    except APIKeyException:
        assert True
    
    except Exception as e:
        print('Unhandled exceptions: ', e)
        assert False