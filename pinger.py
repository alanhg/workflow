"""
判断目标主机群是否处于开机且联网状态

"""

import os

# 打开文件
fo = open("sample/hostnames.txt")
rs = []

for hostname in fo:
    hostname = hostname.strip('\n')
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        rs.append(hostname + ' is up!')
    else:
        rs.append(hostname + ' is down!')

# 关闭文件
fo.close()

print("**************************")
for r in rs:
    print(r)
