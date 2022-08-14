from geox.factory.project_factory import ProjectFactory
from geox.project import Project


class HttpReponseProject():
    def __init__(self, json_response):
        self.project: Project = None
        
        self._factory = ProjectFactory()
        self._parser(json_response)
    
    
    def _parser(self, json_response):
        self.project = self._factory.create(json_response)
