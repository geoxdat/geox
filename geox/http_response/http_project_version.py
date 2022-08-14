from geox.project_version import ProjectVersion
from geox.utils import convert_iso_8601_to_datetime


class HttpReponseProjectVersion():
    def __init__(self, json_response):
        self.project_version: ProjectVersion = None
        
        self._parser(json_response)
    
    
    def _parser(self, json_response):
        self.project_version = self._create_project_version(json_response)
        
    
    def _create_project_version(self, data: dict) -> ProjectVersion:
        project_version = None
        hash = data['project_version_hash'] if 'project_version_hash' in data else None
        if hash:
            project_version = ProjectVersion(hash)
                
            project_version.id = data['project_version_id'] if 'project_version_id' in data else None
            project_version.created_at = convert_iso_8601_to_datetime(data['created_at']) if 'created_at' in data else None
            
            project_version.num_of_collar_rows = data['num_of_collar_rows'] if 'num_of_collar_rows' in data else None
            project_version.num_of_survey_rows = data['num_of_survey_rows'] if 'num_of_survey_rows' in data else None
            project_version.num_of_alteration_rows = data['num_of_alteration_rows'] if 'num_of_alteration_rows' in data else None
            project_version.num_of_assay_rows = data['num_of_assay_rows'] if 'num_of_assay_rows' in data else None
            project_version.num_of_litho_rows = data['num_of_litho_rows'] if 'num_of_litho_rows' in data else None
            project_version.num_of_mineralisation_rows = data['num_of_mineralisation_rows'] if 'num_of_mineralisation_rows' in data else None

        return project_version