#目的：requests库+正则表达式，爬取电影名称、主演、上映日期
# 请求网站：http://maoyan.com/board/4
import requests
import re
import time
import pymongo
def crawler_regular():
    client = pymongo.MongoClient('localhost', connect=False)
    db = client['maoyan']

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}
    for url in range(0, 100, 10):
        url = 'http://maoyan.com/board/4?offset=' + str(url)
        print(url)
        response = requests.get(url, headers=headers)
        res = response.text
        pattern = '<div.*?<p.*?><a.*?>(.*?)</a></p>.*?<p.*?>.*?主演：(.*?)</p>.*?上映时间：(.*?)</p>.*?</div>'
        mmm = re.findall(pattern, res, re.S)  # re.S忽略换行，把字符串作为一个整体
        # print(mmm)
        for m in mmm:
            # print(m)
            info = {'电影名称': m[0], '电影主演': m[1].strip('      '), '上映时间': m[2].strip()}
            db['maoyan'].insert(info)
        print('success')


start_time = time.time()
crawler_regular()
end_time = time.time()
print('cost time is: ', end_time-start_time) # 串行：cost time is:  1.2146430015563965
