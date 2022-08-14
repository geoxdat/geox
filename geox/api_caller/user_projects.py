from geox.connection import connect_to_endpoint
from geox.entity.api_endpoint import APIEndpoint
from geox.http_response.user_projects import HttpReponseUserProjects


def get_user_projects(api_key: str) -> HttpReponseUserProjects:
    response = connect_to_endpoint(
        url=APIEndpoint.GET_USER_PROJECTS,
        method='GET',
        headers={
            "api-key": api_key,
        }
    )
    
    return HttpReponseUserProjects(response)
    
    