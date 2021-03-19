import requests

url = "https://app.dewu.com/api/v1/app/user_core/users/unionLogin"

payload={
        'code': '3885',
        'countryCode': '86',
        'loginToken': '',
        'newSign': '0e00de99d14d36a6088c0aeb80e1c2b6',
        'platform': 'android',
        'sourcePage': '',
        'timestamp': '1615947505015',
        'type': 'code',
        'userName': '15367312074',
        'uuid': '4e7715a9f6933b09',
        'v': '4.64.1'
         }
files=[

]
headers = {
  'duuuid': '4e7715a9f6933b09',
  'duimei': '863125031334635',
  'duplatform': 'android',
  'appId': 'duapp',
  'duchannel': 'pp',
  'duv': '4.64.1',
  'duloginToken': '',
  'dudeviceTrait': 'EVA-AL00',
  'dudeviceBrand': 'HUAWEI',
  'timestamp': '1615947505015',
  'shumeiid': '20210315185332d65f10b73ad3b4f8565d05aecfa68375016167a1cd4499ca',
  'oaid': 'ffbf7d57-7fda-f596-cfce-d7dfdfebfa9a',
  'User-Agent': 'duapp/4.64.1(android;7.0)',
  'X-Auth-Token': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiNGU3NzE1YTlmNjkzM2IwOSIsInVzZXJJZCI6MTYxNjY2MjY1NywiaXNHdWVzdCI6dHJ1ZSwiZXhwIjoxNjQ3NDgzMjkzLCJpYXQiOjE2MTU5NDcyOTMsImlzcyI6IjRlNzcxNWE5ZjY5MzNiMDkiLCJzdWIiOiI0ZTc3MTVhOWY2OTMzYjA5In0.ieoEisrYWBcV7g18xE1JV-EtfnmiNcQc_BeFWWz19iU1teNywc8ebGE_m6l2vK2_sIzDQysS5Qo-OmRiudFekGIazOorTh-sGiPnGZwA312_PMPEqmGPGHFynV8M46os4ZEwSG0kFjLyLZFBlEX_2iv9vuxERCz1vlrR6zBqFri3aMpLv1BvGuLEykfcRLAWCcOAG4GkZ8o_knexq2L_FRGhaujq7ocnLY8vYzZVBzcSbTju2C36h2vJgIlJ6eHLFWyLYLmYb-x6El7W9dQ_cgS55Q3htJJlZs1malll7ZN5KAXutR7ZVZ1c2wxJLt7Ujp_TJpkFqki6Uenbs28wMQ',
  'isRoot': '1',
  'emu': '0',
  'isProxy': '0',
  'Content-Type': 'application/json; charset=utf-8',
  'Transfer-Encoding': 'chunked',
  'Host': 'app.dewu.com',
  'Connection': 'keep-Alive',
  'Accept-Encoding': 'gzip'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files, timeout=1)

print(response.text)
