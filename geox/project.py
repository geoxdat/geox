from datetime import datetime
from geox.api_caller.get_project_version import get_project_version
from geox.api_caller.get_project_versions import get_project_versions
from geox.exceptions import APIKeyException, ProjectIDException
from geox.project_version import ProjectVersion
from typing import List


class Project:
    """Project, defined by project id, may contain various project versions
    """
    def __init__(self, project_id: str):
        self._check_project_id(project_id)
        
        self.project_id: str = project_id
        
        self.title: str = None
        self.location: str = None
        self.description: str = None
        self.created_at: datetime = None
        self.updated_at: datetime = None
        self.num_of_project_versions: int = None
        
        self.project_versions: List[ProjectVersion] = None
        
        # private variables
        self._api_key = None
        self._timestamp = datetime.now()
    
    
    def _check_project_id(self, project_id: str) -> None:
        if not project_id: raise ProjectIDException('Project ID is None or invalid')
        if not isinstance(project_id, str): raise ProjectIDException('Project ID should be a string')
    
    
    def _check_api_key(self, api_key):
        if not api_key: raise APIKeyException('API Key cannot be None')
        if not isinstance(api_key, str): raise APIKeyException('API Key should be string')
    
    
    def set_api_key(self, api_key: str) -> None:
        self._api_key = api_key
        
        
    def read_all_project_versions(self) -> List[ProjectVersion]:
        """Read all project versions of this project

        Returns:
            List[Project]: List of Project Versions
        """
        self._check_api_key(self._api_key)
        http_response = get_project_versions(self._api_key, self.project_id)
        self.project_versions = http_response.project_versions
        return self.project_versions


    def read_project_version(self, hash: str) -> ProjectVersion:
        """Read specific project version

        Args:
            hash (str): project version hash

        Returns:
            ProjectVersion: Project Version object
        """
        self._check_api_key(self._api_key)
        http_response = get_project_version(self._api_key, hash)
        if http_response.project_version: http_response.project_version.set_api_key(self._api_key)
        return http_response.project_version
