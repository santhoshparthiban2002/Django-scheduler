from apscheduler.schedulers.background import BackgroundScheduler
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from .models import Job, JobExecution
from .jobs import *

def run_job(job, function,year,month,day,hour,minute,second):
    job_execution = JobExecution.objects.create(job=job, status='running')
    try:
        function()
        job_execution.status = 'success'
        job_execution.error = 'No Error'
        job = Job.objects.get(pk=job.pk)
        time_interval = relativedelta(years=year, months=month, days=day, hours=hour, minutes=minute, seconds=second)
        job.next_run_time = timezone.now()+time_interval
        job.save()
    except Exception as e:
        job_execution.error = str(e)
        job_execution.status = 'failed'
    finally:
        job_execution.save()

scheduler = BackgroundScheduler(timezone=timezone.get_current_timezone())

job1, created = Job.objects.get_or_create(job_name='print Hello')
job2, created = Job.objects.get_or_create(job_name='print Time')

if created or Job.objects.filter(job_name=job1).exists():
    scheduler.add_job(run_job, 'cron', args=[job1, print_hello,0,0,0,0,1,0], minute="*", second=30)

if created or Job.objects.filter(job_name=job2).exists():
    scheduler.add_job(run_job, 'cron', args=[job2, print_time,0,0,0,1,0,0], hour="*", minute="5", second=30)

scheduler.start()