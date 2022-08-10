from datetime import datetime
from typing import List

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
        
        
    def read_all_projects(self):
        ...


    def read_project(self, project_id: str):
        ...


    def version(self):
        return VERSION

