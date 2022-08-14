from geox.factory.project_factory import ProjectFactory
from geox.project import Project
from typing import List


class HttpReponseProjects():
    def __init__(self, json_response):
        self.projects: List[Project] = None
        
        self._factory = ProjectFactory()
        self._parser(json_response)
    
    
    def _parser(self, json_response):
        if 'projects' in json_response:
            self.projects = []
            for project_data in json_response['projects']:
                project_obj = self._factory.create(project_data)
                if project_obj: self.projects.append(project_obj)
