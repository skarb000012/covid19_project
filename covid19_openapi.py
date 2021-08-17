import requests
from pprint import pprint
from datetime import date, timedelta
import xmltodict
import json

def get_city_data():
    url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson"
    params ={
        'serviceKey':'SBHYNFQv/qb1EqAsg2LpInlGWW3mYt3NeIpMplXnplOOPrGSmCkw2DY6QDApkgbfx/14o6OYsRY5L73iFtOZnw==',
        'pageNo': '1',
        'numOfRows': '30',
        'startCreatDt' : '20210802',
        'endCreatDt': '20210803',
    }

    res = requests.get(url, params=params)

    dict_data = xmltodict.parse(res.text)
    print(dict_data)

    json_data = json.dumps(dict_data)
    dict_data = json.loads(json_data)
    return dict_data["response"]["body"]["items"]["item"]
#print(get_city_data())
    