"""
定时任务，按照既定计划，重复执行某些动作
"""
import schedule
import time

# 执行任务
def job():
    print("I'm working...")

schedule.every(1).seconds.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)