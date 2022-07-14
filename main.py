import schedule
from Job import Job
from Parser import parse

args = parse()

job = Job(
    args.database,
    args.user,
    args.password
)

schedule.every(args.interval).minutes.do(job.work)
while True:
    schedule.run_pending()
