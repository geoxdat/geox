from typing import List
from geox.project_version import ProjectVersion
from geox.utils import convert_iso_8601_to_datetime


class HttpReponseProjectVersions():
    def __init__(self, json_response):
        self.project_versions: List[ProjectVersion] = None
        
        self._parser(json_response)
    
    
    def _parser(self, json_response):
        if 'project_versions' in json_response:
            self.project_versions = []
            for project_data in json_response['project_versions']:
                project_version_obj = self._create_project_version(project_data)
                if project_version_obj: self.project_versions.append(project_version_obj)
            
    
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