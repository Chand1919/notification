
#  Notification Prioritization Engine

##  Overview

This project implements a rule-based **Notification Prioritization Engine** built using FastAPI.

The system evaluates each incoming notification event and classifies it into one of the following categories:

* **NOW** – Send immediately
* **LATER** – Defer or schedule
* **NEVER** – Suppress

The goal is to reduce alert fatigue, prevent duplicate notifications, and ensure important notifications are delivered reliably.

---

## ⚙️ Core Features

* Duplicate Detection (per-user message cache)
* Expiry Validation (suppresses expired notifications)
* Alert Fatigue Protection

  * Maximum 5 notifications per 10 minutes per user
* Priority-Based Decision Engine
* Structured Logging
* REST API using FastAPI
* Modular Service-Based Architecture

---

## 🏗 Architecture Flow

Incoming Event
→ Duplicate Check
→ Expiry Check
→ Alert Fatigue Check
→ Priority Rule Evaluation
→ Final Decision (NOW / LATER / NEVER)

---

## Project Structure

```
notification_engine/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── decision_engine.py
│   ├── services/
│   │     ├── duplicate_service.py
│   │     └── history_service.py
│   ├── config.py
│   └── logger.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How to Run the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start the Server

```bash
python -m uvicorn app.main:app --reload
```

### Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## Sample Test Payload

```json
{
  "user_id": "101",
  "event_type": "security",
  "message": "Suspicious login attempt",
  "priority_hint": "high",
  "timestamp": "2026-02-26T10:00:00",
  "channel": "push"
}
```

---

## Decision Logic Summary

* If duplicate → **NEVER**
* If expired → **NEVER**
* If user received 5 notifications in last 10 minutes → **LATER**
* If priority is high → **NOW**
* Otherwise → **LATER**

---

## Future Improvements (Production-Level Enhancements)

* Redis for distributed duplicate detection
* PostgreSQL for persistent storage
* AI-based importance scoring
* Asynchronous processing for high event volume
* Configurable rule management dashboard
* Monitoring & metrics integration (Prometheus/Grafana)

---

##  Technical Highlights

* Clean modular architecture
* Service-layer separation
* Configurable constants
* Logging for traceability
* Scalable design approach

---

## 🔗 GitHub Repository

You can view the complete source code here:

[View on GitHub](https://github.com/chand1919/notification_engine)


https://github.com/Chand1919/notification.git