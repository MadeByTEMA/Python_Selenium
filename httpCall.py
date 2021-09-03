import requests

def getHttpsGetCall(url: str , params: dict):
    str: str  = ''
    for key in params.keys():
        value = params.get(key)
        if (str == ''):
            str += '?' + key + '=' + value
        else:
            str = '&' + key + '=' + value
    return requests.get(url + str).text

def getHttpsPostCall(url: str , params: dict):
    return requests.post(url + str, data=params).text