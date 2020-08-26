
from requests_html import HTMLSession
hs = HTMLSession()
url="https://pic.mfkhm.com/book/2982/89110/a1052457e5735d661d94810fe56be17f.jpg"
headers=""

for i in range(1, 6):
    try:
        url_response = hs.get(url=url, headers=headers, timeout=5, verify=False)
        print("请求网址：%s" % url)
        print(url_response.content)
        with open('1.png', 'wb') as f:
            f.write(url_response.content)
        break
    except Exception as e:
        print("获取页面请求响应超时异常：%s" % e)
        print("第%s次请求响应超时..." % i)
        continue