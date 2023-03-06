from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
from .models import Job, JobExecution
from .jobs import *

def run_job(job, function,a):
    job_execution = JobExecution.objects.create(job=job, status='running')
    try:
        function()
        job_execution.status = 'success'
        job = Job.objects.get(pk=job.pk)
        job.next_run_time = timezone.now()+timezone.timedelta(seconds=a)
        job.save()
    except Exception as e:
        job_execution.error = str(e)
        job_execution.status = 'failed'
    finally:
        job_execution.save()

scheduler = BackgroundScheduler(timezone=timezone.get_current_timezone())

job1, created = Job.objects.get_or_create(job_name='print')
if created or Job.objects.filter(job_name=job1).exists():
    scheduler.add_job(run_job, 'cron', args=[job1, prints,30], minute="*", second=30)
scheduler.start()
