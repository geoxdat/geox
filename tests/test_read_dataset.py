from geox import GeoX
from geox.exceptions import APIKeyException, ServerErrorException 
import pytest


@pytest.mark.parametrize('api_key, project_id, hash', [
    ['iI5NXd5VvrblQ4RBpssF3PReuOQMLP9U', 'TST000', 'qYTqTkiPfOY45o4gHNUBzcgcpHjqSzbG'],
    ['wrong api key', 'WRONG', 'WRONG'],
    ])
def test_read_collar_dataset(api_key: str, project_id: str, hash: str):
    try:
        geox = GeoX(api_key=api_key)
        project = geox.read_project(project_id)
        project_version = project.read_project_version(hash)
        df_collar = project_version.read_collar_data(save_to_file=False)
        df_survey = project_version.read_survey_data(save_to_file=False)
        df_alteration = project_version.read_alteration_data(save_to_file=False)
        df_assay = project_version.read_assay_data(save_to_file=False)
        df_litho = project_version.read_litho_data(save_to_file=False)
        df_mineralisation = project_version.read_mineralisation_data(save_to_file=False)
        
        assert df_collar is not None
        assert df_survey is not None
        assert df_alteration is not None
        assert df_assay is not None
        assert df_litho is not None
        assert df_mineralisation is not None
    
    except ServerErrorException:
        assert False
        
    except APIKeyException:
        assert True
    
    except Exception as e:
        print('Unhandled exceptions: ', e)
        assert False