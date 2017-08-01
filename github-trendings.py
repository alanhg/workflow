"""
爬取github-trendings上最受欢迎的项目
邮件给目标邮箱
"""
import requests
from bs4 import BeautifulSoup

targetUrl = "https://github.com/trending"
r = requests.get(targetUrl, verify=True)
soup = BeautifulSoup(r.text, "html.parser")
olObj = soup.find('ol', class_="repo-list")

for liObj in olObj.children:
    print(liObj)
# .div.h3.a.span.string