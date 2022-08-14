from geox import GeoX
from geox.exceptions import APIKeyException 
import pytest


@pytest.mark.parametrize('api_key, project_id, hash, is_projects_loaded', [
    ['iI5NXd5VvrblQ4RBpssF3PReuOQMLP9U', 'TST000', 'qYTqTkiPfOY45o4gHNUBzcgcpHjqSzbG', True],
    ['iI5NXd5VvrblQ4RBpssF3PReuOQMLP9U', 'TST000', 'WRONG', False],
    ['iI5NXd5VvrblQ4RBpssF3PReuOQMLP9U', 'WRONG', 'qYTqTkiPfOY45o4gHNUBzcgcpHjqSzbG', False],
    ['wrong api key', 'TST000', 'qYTqTkiPfOY45o4gHNUBzcgcpHjqSzbG', False],
    ['wrong api key', 'TST000', 'WRONG', False],
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