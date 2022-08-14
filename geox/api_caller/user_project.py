from geox.connection import connect_to_endpoint
from geox.entity.api_endpoint import APIEndpoint
from geox.http_response.user_project import HttpReponseUserProject


def get_user_project(api_key: str, project_id: str) -> HttpReponseUserProject:
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
    
    return HttpReponseUserProject(response)
    
    