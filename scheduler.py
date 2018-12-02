from crontab import CronTab
from datetime import time



print("Requesting from Google Calendar ")
print("Unpacking from Google Calendar")

file_cron = CronTab(tabfile='testtab.tab')
mem_cron = CronTab(tab="""
  * * * * * command
""")

job = file_cron.new(command='/home/pranav/piproject/alarmwithCNIT180questions/alarm.py')

job.setall(time(8, 30))


print("making cron job")

