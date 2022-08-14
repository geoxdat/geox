import pytest
from geox import GeoX 


@pytest.mark.parametrize('api_key, is_projects_loaded', 
                         [['iI5NXd5VvrblQ4RBpssF3PReuOQMLP9U', True],
                          ['wrong api key', False]]
                         )
def test_read_projects(api_key: str, is_projects_loaded: bool):
    geox = GeoX(api_key=api_key)
    geox.read_all_projects()
    assert (geox.projects is not None) == is_projects_loaded