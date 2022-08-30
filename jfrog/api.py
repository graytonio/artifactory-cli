from urllib.parse import urljoin
import requests
from jfrog.config import get_config

class AuthError(Exception):
    pass

class RequestError(Exception):
    pass

def api_get_request(path: str):
    access_key = get_config('auth', 'access_token')
    url = get_config("auth", "url")
    username = get_config("auth", "username")
    if access_key == None or url == None or username == None:
        raise AuthError("Config Malformed use jf login to Reauthenticate")
    
    results = requests.get(urljoin(url, path), headers={ 'Authorization': 'Bearer {}'.format(access_key)})
    try:
        data = results.json()
        if 'errors' in data:
            raise RequestError(data['errors'])
    except RequestError as err:
        raise err
    except requests.exceptions.JSONDecodeError:
        pass
    
    return results

def api_post_request(path: str, json: dict):
    access_key = get_config('auth', 'access_token')
    url = get_config("auth", "url")
    username = get_config("auth", "username")
    if access_key == None or url == None or username == None:
        raise AuthError("Config Malformed use jf login to Reauthenticate")
    
    results = requests.post(urljoin(url, path), json=json, headers={ 'Authorization': 'Bearer {}'.format(access_key)})
    
    try:
        if results.status_code >= 300 or results.status_code < 200:
            raise RequestError(results.text)
        
        data = results.json()
        if 'errors' in data:
            raise RequestError(data['errors'])
    except RequestError as err:
        raise err
    except requests.exceptions.JSONDecodeError:
        pass
    
    return results

def api_put_request(path: str, json: dict):
    access_key = get_config('auth', 'access_token')
    url = get_config("auth", "url")
    username = get_config("auth", "username")
    if access_key == None or url == None or username == None:
        raise AuthError("Config Malformed use jf login to Reauthenticate")
    
    results = requests.put(urljoin(url, path), json=json, headers={ 'Authorization': 'Bearer {}'.format(access_key)})
    
    try:
        if results.status_code >= 300 or results.status_code < 200:
            raise RequestError(results.text)
        
        data = results.json()
        if 'errors' in data:
            raise RequestError(data['errors'])
    except RequestError as err:
        raise err
    except requests.exceptions.JSONDecodeError:
        pass
    
    return results

def api_delete_request(path: str):
    access_key = get_config('auth', 'access_token')
    url = get_config("auth", "url")
    username = get_config("auth", "username")
    if access_key == None or url == None or username == None:
        raise AuthError("Config Malformed use jf login to Reauthenticate")
    
    results = requests.delete(urljoin(url, path), headers={ 'Authorization': 'Bearer {}'.format(access_key)})
    
    try:
        if results.status_code >= 300 or results.status_code < 200:
            raise RequestError(results.text)
        
        data = results.json()
        if 'errors' in data:
            raise RequestError(data['errors'])
    except RequestError as err:
        raise err
    except requests.exceptions.JSONDecodeError:
        pass
    
    return results