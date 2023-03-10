# Generated by Django 4.1.7 on 2023-03-07 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=100)),
                ('next_run_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobExecution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runtime', models.DateTimeField(auto_now_add=True)),
                ('error', models.TextField(blank=True, null=True)),
                ('status', models.CharField(max_length=100)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.job')),
            ],
        ),
    ]
