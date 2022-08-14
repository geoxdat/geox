from geox.connection import connect_to_endpoint
from geox.entity.api_endpoint import APIEndpoint
from geox.http_response.http_project import HttpReponseProject


def get_project(api_key: str, project_id: str) -> HttpReponseProject:
    response = connect_to_endpoint(
        url=APIEndpoint.GET_PROJECT,
        method='GET',
        headers={
            "api-key": api_key,
        },
        params={
            'project_id': project_id
        }
    )
    
    return HttpReponseProject(response)
    
    