import requests
from datetime import datetime, timedelta
from time import sleep


def get_questions(days: int, tag: str) -> list:
    url = 'https://api.stackexchange.com/2.3/questions'
    todate = int(datetime.now().timestamp())
    fromdate = int((datetime.now() - timedelta(days=days)).timestamp())
    params = {
        'site': 'stackoverflow',
        'order': 'desc',
        'sort': 'activity',
        'fromdate': fromdate,
        'todate': todate,
        'tagged': tag,
        'page': 1,
        'pagesize': 100
    }
    result = []
    while True:
        response = requests.get(url, params=params).json()
        for item in response['items']:
            result.append(item['title'])
        if not response['has_more']:
            break
        params['page'] += 1
        sleep(0.5)
    return result


if __name__ == '__main__':
    print(*get_questions(2, 'python'))
