from datetime import datetime
from typing import List
from geox.api_caller.initial_auth import call_initial_auth

from geox.project import Project
from geox.version import VERSION


class GeoX:
    def __init__(self, api_key: str):
        self.api_key: str = api_key
        
        self.email: str = None
        self.projects: List[Project] = None
        self.num_of_projects: int = None
        
        # private variables
        self._is_authenticated: bool = False
        self._timestamp = datetime.now()
        
        self._initial_auth()
    
    
    def _initial_auth(self):
        if not self._is_authenticated:
            http_response = call_initial_auth(self.api_key)
            self.email = http_response.email
            self.num_of_projects = http_response.num_of_projects
            self._is_authenticated = True
        
        
    def read_all_projects(self):
        ...


    def read_project(self, project_id: str):
        ...


    def version(self):
        return VERSION

