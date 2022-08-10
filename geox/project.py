from datetime import datetime


class Project:
    def __init__(self, project_id: str):
        self.project_id: str = project_id
        
        self.title: str = None
        self.location: str = None
        self.description: str = None
        self.created_at: str = None
        self.updated_at: str = None
        self.datasets: str = None
        self.num_of_datasets: str = None
        
        # private variables
        self._is_updated: bool = False
        self._timestamp = datetime.now()
        
        
    def read_all_project_versions(self):
        ...


    def read_project_version(self, hash: str):
        ...

