from geox.connection import connect_to_endpoint
from geox.entity.api_endpoint import APIEndpoint
from geox.http_response.initial_auth import HttpReponseInitialAuth


def call_initial_auth(api_key: str) -> HttpReponseInitialAuth:
    response = connect_to_endpoint(
        url=APIEndpoint.GET_INITIAL_AUTH,
        method='GET',
        headers={
            "api-key": api_key,
        }
    )
    
    return HttpReponseInitialAuth(response.json())