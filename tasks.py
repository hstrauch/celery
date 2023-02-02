import os
from celery import Celery
from celery.utils.log import get_task_logger
import time

app = Celery('tasks', broker=os.getenv("CELERY_BROKER_URL"))
logger = get_task_logger(__name__)


@app.task
def add(x, y):
    ttimes = 1
    while ttimes < 100:
        logger.info(f'Showed {ttimes} times')
        ttimes += 1
        time.sleep(10)
    #logger.info(f'Adding {x} + {y}')
    return x + y
