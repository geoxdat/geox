from geox import GeoX
from geox.exceptions import APIKeyException 
import pytest


@pytest.mark.parametrize('api_key, project_id, is_project_loaded', [
    ['iI5NXd5VvrblQ4RBpssF3PReuOQMLP9U', 'TST000', True],
    ['iI5NXd5VvrblQ4RBpssF3PReuOQMLP9U', 'WRONG', False],
    ['wrong api key', 'TST000', False],
    ['wrong api key', 'WRONG', False],
    [None, None, False],
    ])
def test_read_project(api_key: str, project_id: str, is_project_loaded: bool):
    try:
        geox = GeoX(api_key=api_key)
        project = geox.read_project(project_id)
        assert (project is not None) == is_project_loaded
    
    except APIKeyException:
        assert True
    
    except Exception as e:
        print('Unhandled exceptions: ', e)
        assert False