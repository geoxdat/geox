from time import sleep
from geox.exceptions import APIKeyException, ParameterException, ServerErrorException
from http import HTTPStatus
from requests import request, Response
from requests.exceptions import ConnectionError


def check_status_code(response: Response) -> None:
    '''checking all available status code from GeoX API'''
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        raise APIKeyException(f'Unauthorized. {response.json()["detail"]}.')
    
    elif response.status_code == HTTPStatus.BAD_REQUEST:
        raise ParameterException(f'Some of the parameter in request is invalid. {response.text}.')
    
    elif response.status_code == HTTPStatus.NOT_FOUND:
        raise ServerErrorException('404. Not Found response, server error.')

def connect_to_endpoint(url: str, method: str, headers: dict={}, params:dict ={}) -> dict:
    '''Connect to endpoint'''
    try:
        response = request(
            method=method, 
            url=url, 
            headers = headers, 
            params = params,
            verify=False,
            )
        
        # checking status code
        check_status_code(response)

        return response.json()
    
    except ParameterException as e:
        print(e)
        # sys.exit()
        return {}
    
    except ConnectionError as e:
        print('Connection Error. Retrying in 5 seconds')
        sleep(5)
        return connect_to_endpoint(url, method, headers, params)