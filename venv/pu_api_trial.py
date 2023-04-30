import os

import requests
import json
import jsonpath


def test_put_data():
    # APi path
    url = "https://reqres.in/api/users/2"
    json_path = os.getcwd() + "/myputdata.json"
    str_json_file_obj = open(json_path, mode='r')
    str_json_file_data = str_json_file_obj.read()
    # converting str to dic
    json_file_data = json.loads(str_json_file_data)
    res_obj = requests.put(url, json_file_data)
    res_status_code = res_obj.status_code
    assert res_status_code == 200
