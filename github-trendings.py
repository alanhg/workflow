"""
爬取github-trendings上最受欢迎的项目
邮件给目标邮箱
"""
import requests
from bs4 import BeautifulSoup

targetUrl="https://github.com/trending"
r = requests.get(targetUrl, verify=True)
soup=BeautifulSoup(r.text)

ol=soup.find_all("ol", class_="repo-list")
print(ol[0])

