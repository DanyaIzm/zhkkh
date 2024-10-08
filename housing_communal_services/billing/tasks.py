from celery import shared_task


@shared_task
def debug_task(aboba):
    print(f'Absoothinque, {aboba}')