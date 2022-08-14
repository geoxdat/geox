from geox.factory.project_version_factory import ProjectVersionFactory
from geox.project_version import ProjectVersion


class HttpReponseProjectVersion():
    def __init__(self, json_response):
        self.project_version: ProjectVersion = None
        
        self._factory = ProjectVersionFactory()
        self._parser(json_response)
    
    
    def _parser(self, json_response):
        self.project_version = self._factory.create(json_response)
