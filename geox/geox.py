from datetime import datetime
from typing import List
from geox.api_caller.get_initial_auth import get_initial_auth
from geox.api_caller.get_project import get_project
from geox.api_caller.get_projects import get_projects
from geox.exceptions import APIKeyException

from geox.project import Project
from geox.version import VERSION


class GeoX:
    def __init__(self, api_key: str):
        self._check_api_key(api_key)
        
        self.api_key: str = api_key
        
        self.email: str = None
        self.projects: List[Project] = None
        self.num_of_projects: int = None
        
        # private variables
        self._timestamp = datetime.now()
        
        self._initial_auth()
    
    
    def _check_api_key(self, api_key):
        if not api_key: raise APIKeyException('API Key cannot be None')
        if not isinstance(api_key, str): raise APIKeyException('API Key should be string')
    
        
    def _initial_auth(self):        
        http_response = get_initial_auth(self.api_key)
        self.email = http_response.email
        self.num_of_projects = http_response.num_of_projects
        
        
    def read_all_projects(self) -> List[Project]:
        if not self.email: return
        http_response = get_projects(self.api_key)
        self.projects = http_response.projects
        return self.projects


    def read_project(self, project_id: str) -> Project:
        if not self.email: return
        http_response = get_project(self.api_key, project_id)
        if http_response.project: http_response.project.set_api_key(self.api_key)
        return http_response.project


    def version(self):
        return VERSION

