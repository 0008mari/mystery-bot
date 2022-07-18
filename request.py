# request

import requests
import json
from urllib.parse import urlencode


# input: none
# output: json of recent 
def request():

    url_origin = "http://www.aladin.co.kr/ttb/api/ItemList.aspx?"
    params = {
        'TTBKey': 'ttb00mari2308001',
        'QueryType': 'ItemNewAll',
        'MaxResults': '20',
        'Sort': 'PublishTime',
        'CategoryId': '50926',
        'ItemIdType': 'ISBN13',
        'Cover': 'MidBig',
        'Output': 'JS',
        'Version': '20131101',
    }
    query_string = url_origin + urlencode(params)

    answer = requests.get(query_string).text
    answer.encode("utf-8")
    dict = json.loads(answer)
    return dict


# request() 
