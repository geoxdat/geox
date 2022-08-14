from geox.connection import connect_to_endpoint
from geox.entity.api_endpoint import APIEndpoint
from geox.http_response.http_project_version import HttpReponseProjectVersion


def get_project_version(api_key: str, hash: str) -> HttpReponseProjectVersion:
    response = connect_to_endpoint(
        url=APIEndpoint.GET_PROJECT_VERSION,
        method='GET',
        headers={
            "api-key": api_key,
        },
        params={
            'hash': hash
        }
    )
    
    return HttpReponseProjectVersion(response)
    
    