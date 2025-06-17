# main.py

"""
noti-py: A lightweight desktop notification scheduler
Author: wewegahyun@gmail.com
"""

from plyer import notification
from datetime import datetime, timedelta
import time

# Notification content
TITLE = "[noti-py] Time to check!"
MESSAGE = "1. git push \n2. SageMaker Notebook off"


def send_notification(title=TITLE, message=MESSAGE):
    """
    Send a desktop notification with a given title and message.
    """
    notification.notify(
        title=title,
        message=message,
        app_name='noti-py',
        timeout=10
    )


def schedule_notification(hour: int, minute: int):
    """
    Wait until the specified hour and minute, then send the notification.
    """
    now = datetime.now()
    notify_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

    # If the scheduled time has already passed today, set it for tomorrow
    if notify_time < now:
        notify_time += timedelta(days=1)

    time_to_wait = (notify_time - now).total_seconds()
    time.sleep(time_to_wait)
    send_notification()


if __name__ == "__main__":
    # Set your desired notification time (e.g., 4:50 PM)
    schedule_notification(hour=16, minute=50)
