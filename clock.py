import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()
# Very basic examples here
# https://devcenter.heroku.com/articles/clock-processes-python

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    print('This job is run every three minutes.')
    print(datetime.datetime.now())

# @sched.scheduled_job('cron', day_of_week='mon-sun', hour=14)
# def scheduled_job():
#     print('This job is run every weekday at 2pm.')

sched.start()
