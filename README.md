# noti-py 🛎️

> **noti-py**, a playful take on `notify`, is a **customizable desktop notification assistant** that alerts you at your scheduled time.

---

## Overview

**noti-py** is a lightweight tool that helps you stay on track by sending time-based desktop notifications. It’s useful for:

- End-of-day task reminders
- Git push notifications
- Cloud instance shutdown reminders
- Any personalized time-based alerts

Simply set the time, and **noti-py** will pop up a notification window with your custom message. Both the message and title are fully configurable.

---

## Execution Pipeline

### 1. Install dependencies

```bash
pip install plyer
```

### 2. Customize your message and time
Open main.py and update the following variables as needed:

```python
# Set your custom notification content
TITLE = "[noti-py] Time to check!"
MESSAGE = "1. git push \n2. Turn off your cloud notebook"

# Set your desired notification time (e.g., 4:50 PM)
schedule_notification(hour=16, minute=50)
```

### 3. Run the script

```bash
python main.py
```
