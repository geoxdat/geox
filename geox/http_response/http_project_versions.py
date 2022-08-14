from geox.factory.project_version_factory import ProjectVersionFactory
from geox.project_version import ProjectVersion
from typing import List


class HttpReponseProjectVersions():
    def __init__(self, json_response):
        self.project_versions: List[ProjectVersion] = None
        
        self._factory = ProjectVersionFactory()
        self._parser(json_response)
    
    
    def _parser(self, json_response):
        if 'project_versions' in json_response:
            self.project_versions = []
            for project_data in json_response['project_versions']:
                project_version_obj = self._factory.create(project_data)
                if project_version_obj: self.project_versions.append(project_version_obj)
