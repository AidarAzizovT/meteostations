import requests
import json
data = {
    "page": 1,
    "limit": 78300,
    "filter": [
        {
            "property": "name",
            "value": "км 88+000 a/д Кузайкино-Нурлат (Русское Сиренькино)",
            "operator": "like"
        },
        {
            "property": "date",
            "value": [
                "2020-12-31T21:00:00.000Z",
                "2021-12-31T20:59:59.000Z"
            ],
            "operator": "between"
        }
    ],
    "sorter": {
        "property": "date",
        "direction": "ASC"
    }
}

REQUEST_URL = "https://transportsystem.ru/api/its/meteo_stations/value/list"


result = requests.post(url=REQUEST_URL, data=json.dumps(data), headers = {'Content-type': 'application/json'})

