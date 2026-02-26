from datetime import datetime, timedelta

user_history = {}

def record_notification(user_id: str):
    now = datetime.now()

    if user_id not in user_history:
        user_history[user_id] = []

    user_history[user_id].append(now)


def notification_count_last_10_min(user_id: str):
    now = datetime.now()
    ten_minutes_ago = now - timedelta(minutes=10)

    if user_id not in user_history:
        return 0

    return len([t for t in user_history[user_id] if t > ten_minutes_ago])