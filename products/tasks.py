from celery import shared_task
import time 




@shared_task
def send_emails():
    for x in range(10):
        time.sleep(2)
        print(f'sending email to {x}')