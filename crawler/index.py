import urllib.request
import urllib.parse
from urllib.error import HTTPError
import json
from crawler import config
from crawler import log

base_url = 'https://app.qixin.com/v4/enterprise/advanceSearch2'

keyword = "食品"
page = 1

headers = {
    'platform': 'android',
    'device-id': '868030022559320',
    'push-registration': 'NBSVAB4PEHHDTC55QTCUAdCY',
    'functionsettings-time': '1507441875',
    'session-id': '8273abb3-b5c2-41de-9844-5dd9b442542e',
    'app-version': '3.9.3',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'account': '13776601064',
    'user-id': '59d9bd044dd7157d8f6a9121',
    'syssettings-time': '1506751775',
    'token': '0IbHxSaAkquTU826A9pgEIsGgyUuWzPhP+SZ0AM7lhM1PcQ8LjDX8Dgx9e1iNIDc26aJwx5KdK73fjHxayjHthHKljZbPjClbB7tC0dQTIL8MKtvC7O1P8rrzujukf4num6bV95QUXTCo+FrU4gCEEG1Y+RF3JcovrJe/X0FWak=',
    'User-Agent': config.agent_chrome,
}
# 请求参数

values = {
    'start': 0,
    'method': '',
    'execution_count': '',
    'token': 'CIlCWm8lor3R0YBNvAIOb9eD6zIPLX1lt9ueP48yDk32u%2Beu3lRJc%2FHtguIXO%2FMuly57zynvMzGj5vxq7uyr7w%3D%3D',
    'trademark_count': '',
    'yearTo': '',
    'capiTo': '',
    'domain': '',
    'province': '',
    'cityCode': '',
    'yearFrom': '',
    'capiFrom': '',
    'phone_count': '',
    'sortBy': '',
    'status': '',
    'keyword': keyword,
    'patent_count': '',
    'district': ''
}


def get_html_text(url, data=None, header=None):
    log.d(url)
    if header is None:
        header = {}
    else:
        log.d("headers:" + format_json(headers))
    try:
        if data is not None:
            log.d("data:" + format_json(data))
        data = urllib.parse.urlencode(data).encode('UTF8')
        req = urllib.request.Request(url, data=data, headers=header)
        return urllib.request.urlopen(req).read()
    except HTTPError as e:
        log.e(str(e))


def format_json(data):
    try:
        return json.dumps(data, sort_keys=True, indent=4)
    except Exception as e:
        print(e)
        return None


# get_data()

# result = get_html_text(base_url, data=values)
# print(json.loads(result))
v = "d420d27c5d7f3d3d9a024cb72f861e0be418e133226642575fd517dd536fdff4bed2996cb19459628e86a0bcacdb0ca4797ecd03694009e9b18ea5ca5ea22a42"
print(len(v))