from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime

def scheduler_task():
    # 打印当前时间
    print(f"当前时间：{datetime.now()}")

scheduler = BackgroundScheduler()
scheduler.add_job(scheduler_task, CronTrigger.from_crontab("0 * * * *"))