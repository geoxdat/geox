from typing import List
from geox.project import Project
from geox.utils import convert_iso_8601_to_datetime


class HttpReponseUserProjects():
    def __init__(self, json_response):
        self.projects: List[Project] = []
        
        self._parser(json_response)
    
    
    def _parser(self, json_response):
        for project_data in json_response['projects']:
            project_obj = self._create_project(project_data)
            self.projects.append(project_obj)
            
    
    def _create_project(self, data: dict) -> Project:
        project_id = data['project_id'] if 'project_id' in data else None
        
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