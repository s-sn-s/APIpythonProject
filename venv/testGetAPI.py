import requests
import json
import jsonpath
api_response = requests.get('https://reqres.in/api/users/23')


def test_api_get():
    assert api_response.status_code == 404
    data = api_response.text
    print(data)
    print(type(data))
    json_data = json.loads(data)
    print(json_data)
    assert json_data is not None


def test_api_get_it():
    assert api_response.status_code == 403
