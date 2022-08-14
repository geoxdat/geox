from geox import GeoX
from geox.exceptions import APIKeyException 
import pytest


@pytest.mark.parametrize('api_key, email', [
    ['iI5NXd5VvrblQ4RBpssF3PReuOQMLP9U', 'razifrizqullah@gmail.com'],
    ['wrong api key', None],
    [None, None],
    ])
def test_initialize_geox(api_key: str, email: str):    
    try:
        geox = GeoX(api_key=api_key)
        assert geox.email == email
    
    except APIKeyException:
        assert True
    
    except Exception as e:
        print('Unhandled exceptions: ', e)
        assert False