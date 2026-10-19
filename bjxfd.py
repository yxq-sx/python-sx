import requests
from fake_useragent import UserAgent

def caijia(n):
    url = 'http://www.xinfadi.com.cn/getPriceData.html'
    h = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36 Edg/155.0.0.0',
        'referer': 'http://www.xinfadi.com.cn/index.html'
    }
    data = {
        'limit':'20',
        'current':'2',
        'pubDateStartTime':'2024/01/01',
        'pubDateEndTime':'',
        'prodPcatid': '',
        'prodCatid': '',
        'prodName': '',
    }
    resp = requests.post(url=url, headers=h, data=data)
    resp.encoding = resp.apparent_encoding
    print(resp.status_code)
if __name__ == '__main__':
    for i in range(3):
        print('开始采集第{}页'.format(i))
        caijia(i)
        print('第{}页采集成功'.format(i))
