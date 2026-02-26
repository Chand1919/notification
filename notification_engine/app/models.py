from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class NotificationEvent(BaseModel):
    user_id: str
    event_type: str
    message: str
    priority_hint: Optional[str] = "low"
    timestamp: datetime
    channel: str
    dedupe_key: Optional[str] = None
    expires_at: Optional[datetime] = None