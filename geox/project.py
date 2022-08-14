from datetime import datetime
from typing import List
from geox.exceptions import ProjectIDException

from geox.project_version import ProjectVersion


class Project:
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
        self._timestamp = datetime.now()
    
    
    def _check_project_id(self, project_id: str) -> None:
        if not project_id: raise ProjectIDException('Project ID is None or invalid')
        if not isinstance(project_id, str): raise ProjectIDException('Project ID should be a string')
        
        
    def read_all_project_versions(self):
        ...


    def read_project_version(self, hash: str):
        ...
