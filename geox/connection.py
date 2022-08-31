from geox.exceptions import APIKeyException, ParameterException, ServerErrorException
from http import HTTPStatus
from requests import request, Response, packages
from requests.exceptions import ConnectionError, SSLError
from time import sleep
from urllib3.exceptions import InsecureRequestWarning
import urllib3

urllib3.disable_warnings(InsecureRequestWarning)


def check_status_code(response: Response) -> None:
    '''checking all available status code from GeoX API'''
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        raise APIKeyException(f'Unauthorized. {response.json()["detail"]}.')
    
    elif response.status_code == HTTPStatus.BAD_REQUEST:
        raise ParameterException(f'Some of the parameter in request is invalid. {response.text}.')
    
    elif response.status_code == HTTPStatus.NOT_FOUND:
        raise ServerErrorException('Not Found response.')
    
    elif response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        raise ServerErrorException('Internal server error.')


def connect_to_endpoint(url: str, method: str, headers: dict={}, params:dict ={}, verify_ssl:bool=True) -> dict:
    '''Connect to endpoint'''
    try:
        response = request(
            method=method, 
            url=url, 
            headers = headers, 
            params = params,
            verify=verify_ssl,
            )
        
        # checking status code
        check_status_code(response)

        return response.json()
    
    except ParameterException as e:
        print(e)
        # sys.exit()
        return {}
    
    except SSLError:
        return connect_to_endpoint(url, method, headers, params, verify_ssl=False)
        
    except ConnectionError:
        print('Connection Error. Retrying in 5 seconds')
        sleep(5)
        return connect_to_endpoint(url, method, headers, params)
