from fastapi import FastAPI
from app.models import NotificationEvent
from app.decision_engine import evaluate_notification

app = FastAPI(title="Notification Prioritization Engine")

@app.get("/")
def home():
    return {"message": "Notification Engine Running"}

@app.post("/evaluate")
def evaluate(event: NotificationEvent):
    decision, reason = evaluate_notification(event)

    return {
        "decision": decision,
        "reason": reason
    }