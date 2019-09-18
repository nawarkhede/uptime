from django_cron import CronJobBase, Schedule
import requests
from uptime import models as uptime_models

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code

    def do(self):
        site = uptime_models.Site.objects.get(id=1)
        et = uptime_models.ElapsedTime.objects.create(site=site, time_elapsed=0)
        print('Object created with id %d' % et.id)
        time_elapsed = requests.get("https://stackoverflow.com").elapsed.total_seconds()
        et.time_elapsed = time_elapsed
        print('Object updated with id %d' % et.id)
        et.save()