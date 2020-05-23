# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
# from django_apscheduler.jobstores import register_events, register_job

# from django.conf import settings
# import sportsEquipment.views as views

# # Create scheduler to run in a thread inside the application process
# scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)

# def start():
# 	scheduler.add_job(views.update_penalty, 'interval', seconds=1,misfire_grace_time=10)
# 	register_events(scheduler)
# 	scheduler.start() 