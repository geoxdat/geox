from geox.connection import connect_to_endpoint
from geox.entity.api_endpoint import APIEndpoint
from geox.http_response.http_project_versions import HttpReponseProjectVersions


def get_project_versions(api_key: str, project_id: str) -> HttpReponseProjectVersions:
    response = connect_to_endpoint(
        url=APIEndpoint.GET_PROJECT_VERSIONS,
        method='GET',
        headers={
            "api-key": api_key,
        },
        params={
            'project_id': project_id
        }
    )
    
    return HttpReponseProjectVersions(response)
    
    