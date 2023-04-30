import os

import requests
import json
import jsonpath


def test_post_api():
    url = 'https://reqres.in/api/users'
    json_file = os.getcwd() + '/mypostdata.json'
    json_obj = open(json_file,mode='r')
    json_str = json_obj.read()
    json_dic = json.loads(json_str)
    res_obj = requests.post(url,json_dic)
    assert res_obj.status_code == 201
