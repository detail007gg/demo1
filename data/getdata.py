from bs4 import BeautifulSoup
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import re  # 导入正则
import yaml

# # 发送请求
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# r = requests.get('https://jablehk.com/adult', verify=False)
#
# 将html内容传入BeautifulSoup
# soup = BeautifulSoup(r.content, 'html.parser')
# 通过标签名查找元素
# for link in soup.find_all('img'):
#     print(link.get('data-image'))
# ================================================

proxies = {
    "http": "http://45.207.13.121:80"
}

# url = "https://xxxnnn.org/#random"
url = "https://66mdoe.top/"
headers = {
    "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
response = requests.get(url, proxies=proxies, verify=False, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())
for link in soup.find_all('a'):
        src = link.get('href')
        with open('./sorce.yaml','a+') as f:
            yaml.dump(src,f)


# src=soup.find_all(attrs={'class':"gallery-grid-image-link" ,'data-no-animation':""})
# print(type(src))
# print(src)
# for i in src:
#     title=i.next_sibling()
#     print(title)
# link=i['data-image']
# print({
#     "标题":title,
#     "链接": link
# })

# 读取yaml文件
def read_yaml_file(file):
    with open(file, 'r+') as f:
        y = yaml.load(f, Loader=yaml.FullLoader)
        return y
