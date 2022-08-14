import pytest
from geox import GeoX 


@pytest.mark.parametrize('api_key, project_id, is_project_loaded', 
                         [['iI5NXd5VvrblQ4RBpssF3PReuOQMLP9U', 'TST000', True],
                          ['iI5NXd5VvrblQ4RBpssF3PReuOQMLP9U', 'WRONG', False],
                          ['wrong api key', 'TST000', False],
                          ['wrong api key', 'WRONG', False]]
                         )
def test_read_project(api_key: str, project_id: str, is_project_loaded: bool):
    geox = GeoX(api_key=api_key)
    project = geox.read_project(project_id)
    assert (project is not None) == is_project_loaded