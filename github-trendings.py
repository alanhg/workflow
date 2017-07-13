"""
爬取github-trendings上最受欢迎的项目
邮件给目标邮箱
"""
import requests

targetUrl="https://github.com/trending"
r = requests.get(targetUrl, verify=True)
print(r.text)