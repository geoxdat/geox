from geox.connection import connect_to_endpoint
from geox.entity.api_endpoint import APIEndpoint
from geox.http_response.http_projects import HttpReponseProjects


def get_projects(api_key: str) -> HttpReponseProjects:
    response = connect_to_endpoint(
        url=APIEndpoint.GET_USER_PROJECTS,
        method='GET',
        headers={
            "api-key": api_key,
        }
    )
    
    return HttpReponseProjects(response)
    
    