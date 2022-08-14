from typing import List
from geox.project import Project
from geox.utils import convert_iso_8601_to_datetime


class HttpReponseUserProject():
    def __init__(self, json_response):
        self.project: Project = None
        
        self._parser(json_response)
    
    
    def _parser(self, json_response):
        self.project = self._create_project(json_response)
            
    
    def _create_project(self, data: dict) -> Project:
        project = None
        project_id = data['project_id'] if 'project_id' in data else None
        if project_id:
            project = Project(project_id)
            
            project.title = data['title'] \
                if 'title' in data else None

            project.location = data['location'] \
                if 'location' in data else None

            project.description = data['description'] \
                if 'description' in data else None

            project.num_of_project_versions = data['num_of_project_versions'] \
                if 'num_of_project_versions' in data else None

            project.created_at = convert_iso_8601_to_datetime(data['created_at']) \
                if 'created_at' in data else None

            project.updated_at = convert_iso_8601_to_datetime(data['updated_at']) \
                if 'updated_at' in data else None

        return project