from datetime import datetime
from app.services.duplicate_service import is_duplicate, update_cache
from app.services.history_service import (
    record_notification,
    notification_count_last_10_min,
)
from app.logger import logger
from app.config import MAX_NOTIFICATIONS_PER_10_MIN, HIGH_PRIORITY


def evaluate_notification(event):

    logger.info(f"Evaluating notification for user {event.user_id}")

    # Duplicate check
    if is_duplicate(event.user_id, event.message):
        logger.warning("Duplicate notification detected")
        return "NEVER", "Duplicate notification"

    # Expiry check
    if event.expires_at and event.expires_at < datetime.now():
        logger.warning("Expired notification")
        return "NEVER", "Notification expired"

    # Fatigue check
    count = notification_count_last_10_min(event.user_id)
    if count >= MAX_NOTIFICATIONS_PER_10_MIN:
        logger.info("User fatigue protection triggered")
        return "LATER", "Too many notifications in last 10 minutes"

    # High priority
    if event.priority_hint == HIGH_PRIORITY:
        update_cache(event.user_id, event.message)
        record_notification(event.user_id)
        logger.info("High priority notification sent immediately")
        return "NOW", "High priority notification"

    # Default case
    update_cache(event.user_id, event.message)
    record_notification(event.user_id)
    logger.info("Low priority notification deferred")
    return "LATER", "Low priority notification"