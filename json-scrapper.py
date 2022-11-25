import requests

cookies = {
    'ci_session': 'ljjj3h9gasr3a1gs124vaquj594gb80p',
    'csrf_cookie_name': 'fc8d0dd228c6c624236977ae9aed5225',
}

headers = {
    'Accept': '/',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'ci_session=ljjj3h9gasr3a1gs124vaquj594gb80p; csrf_cookie_name=fc8d0dd228c6c624236977ae9aed5225',
    'Origin': 'https://ngodarpan.gov.in',
    'Referer': 'https://ngodarpan.gov.in/index.php/search',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

stateId = '37'

import json
import os

ids = json.load(open('./ids/'+stateId+'.json'))

for id in ids:
    data = {
        'id': id,
        'csrf_test_name': 'fc8d0dd228c6c624236977ae9aed5225',
    }

    isExist = os.path.exists('./data/'+stateId)
    if not isExist:
        os.mkdir('./data/'+stateId)

    print('downloading', id)
    response = requests.post('https://ngodarpan.gov.in/index.php/ajaxcontroller/show_ngo_info', cookies=cookies, headers=headers, data=data)
    fileName = './data/'+ stateId + '/'+ id + '.json'
    with open(fileName, 'w+') as f:
        f.write(response.text)