import requests
import json
import jsonpath


def test_del_api():
    del_api_res = requests.delete("https://reqres.in/api/users/2")
    print(del_api_res.status_code)
    assert del_api_res.status_code == 204
