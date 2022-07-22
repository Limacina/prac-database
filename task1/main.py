import schedule
from Job import Job
from Parser import parse
from datetime import datetime
import pause

args = parse()

job = Job(
    args.database,
    args.user,
    args.password
)

if args.start:
    pause.until(
        datetime(datetime.today().year,
                 datetime.today().month,
                 datetime.today().day,
                 int(args.start[0:2]),
                 int(args.start[3:5]),
                 int(args.start[6:8]))
    )
schedule.every(args.interval).minutes.do(job.work)
while True:
    schedule.run_pending()
