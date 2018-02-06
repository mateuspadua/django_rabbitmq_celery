from celery import shared_task
import time


@shared_task(ignore_result=True)
def send_email(recepient, title, subject):
    print 'sending email'


@shared_task
def rebuild_search_index():
    time.sleep(3)  # mimicking a long running process
    print 'rebuilt search index'
    return "anything"
