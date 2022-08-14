import pytest
from geox import GeoX 


@pytest.mark.parametrize('api_key, email', 
                         [['iI5NXd5VvrblQ4RBpssF3PReuOQMLP9U', 'razifrizqullah@gmail.com'],
                          ['wrong api key', None]]
                         )
def test_initialize_geox(api_key: str, email: str):
    geox = GeoX(api_key=api_key)
    assert geox.email == email