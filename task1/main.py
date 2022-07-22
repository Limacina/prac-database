import schedule
from Job import Job
from Parser import parse
from datetime import datetime
import pause
import re


args = parse()

job = Job(
    args.database,
    args.user,
    args.password
)

if re.fullmatch('([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]', args.start):
    pause.until(
        datetime(datetime.today().year,
                 datetime.today().month,
                 datetime.today().day,
                 int(args.start[0:2]),
                 int(args.start[3:5]),
                 int(args.start[6:8]))
    )
else:
    print('Start format invalid, assuming current moment')

schedule.every(args.interval).minutes.do(job.work)
while True:
    if job.connected:
        schedule.run_pending()
    else:
        break
