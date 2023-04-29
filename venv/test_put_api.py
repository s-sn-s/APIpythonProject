import requests
import json
import jsonpath


def test_put():
    my_api_link = "https://reqres.in/api/users/2"
    json_file_path = "/Users/savinshetty/PycharmProjects/pythonProject/venv/myputdata.json"
    # print(json_file_path)

    data = open(json_file_path, mode='r')

    datacon = data.read()

    j_data = json.loads(datacon)

    vpr = requests.put(my_api_link, j_data)

    assert vpr.status_code == 200
