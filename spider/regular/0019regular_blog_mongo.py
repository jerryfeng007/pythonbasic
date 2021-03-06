# requests库+正则表达式：博客标题、博客链接、博客时间，存储在mongodb
import requests
import re
import time
import threading
from pymongo import MongoClient


def regular_blog_mongo(i):
    client = MongoClient('localhost', connect=False)
    db = client['blog']
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
    url = 'http://www.xqtesting.com/blog/p' + str(i) + '.html'
    # print(url)
    res = requests.get(url, headers=headers)
    res = res.text
    pattern = '<h4.*?class.*?card-heading.*?>.*?<a.*?href.*?(.*?).html.*?style.*?color:.*?>(.*?)</a>.*?</h4>.*?<i class="icon-time"></i>(.*?)</span>'
    results = re.findall(pattern, res, re.S)
    for result in results:
        # print(result)
        # print(result[0][2:])
        # print(result[1])
        # print(result[2])
        lianjie = 'http://www.xqtesting.com' + result[0][2:] + '.html'
        info = {'博客标题': result[1], '博客链接': lianjie, '博客时间': result[2]}
        db['blog'].insert(info)
        print('success')


start_time = time.time()
for i in range(1, 32):
    t = threading.Thread(target=regular_blog_mongo, args=(i,))
    t.start()
end_time = time.time()
print('cost time:', end_time-start_time)
