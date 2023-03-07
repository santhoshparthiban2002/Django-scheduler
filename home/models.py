from django.db import models

# Create your models here.
class Job(models.Model):
    job_name = models.CharField(max_length=100)
    next_run_time = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.job_name

class JobExecution(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    runtime = models.DateTimeField(auto_now_add=True)
    error = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.job} - {self.runtime}"