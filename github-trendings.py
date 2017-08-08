"""
爬取github-trendings上最受欢迎的项目
邮件给目标邮箱
"""
import requests
from bs4 import BeautifulSoup

from sendEmail import EMailSender

targetUrl = "https://github.com/trending"
r = requests.get(targetUrl, verify=True)
soup = BeautifulSoup(r.text, "html.parser")
olObj = soup.find('ol', class_="repo-list").find_all("li")

print('热门仓库')
for liObj in olObj:
    print(liObj.div.a)

emailSender=EMailSender()

emailSender.send(str(olObj))
