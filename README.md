# 📅 Event Scheduler API

A lightweight Python + Flask REST API to **manage calendar events**: create, list, update, and delete.  
Ideal for learning backend basics, working with JSON data, and practicing API testing.

---

## ⚙️ How to run the project

1️⃣ Clone this repository or download and unzip it.

2️⃣ Install required packages:
```bash
pip install -r requirements.txt
```

3️⃣ Ensure `events.json` file exists with the following initial content:
```json
[]
```

4️⃣ Start the server:
```bash
python app.py
```

Server will run on:
```
http://127.0.0.1:5000
```

---

## 📂 Folder structure

```
event_scheduler/
├── app.py                                  # Flask API with endpoints
├── storage.py                              # Load/save events to JSON
├── events.json                             # JSON file storing events
├── requirements.txt                        # Python dependencies
├── README.md                               # Project documentation
└── Event Scheduler System.postman_collection.json # Postman collection for testing
```

---

## 🧪 Testing with Postman

Instead of a frontend, use Postman to call the API:

1️⃣ Open Postman → **Import**  
2️⃣ Select `Event Scheduler System.postman_collection.json`  
3️⃣ Use these endpoints:

| Method | Endpoint                | Purpose                          |
|------:|------------------------:|---------------------------------:|
| GET   | `/events`               | Get all events (sorted) |
| POST  | `/events`               | Add a new event |
| PUT   | `/events/<event_id>`    | Update an existing event |
| DELETE| `/events/<event_id>`    | Delete an event by ID |

---

## 📌 Sample JSON payload

When creating or updating an event, use:
```json
{
  "title": "My Todays Schedule",
  "description": "Meet to discuss deliverables",
  "start_time": "2025-07-01 14:00",
  "end_time": "2025-07-01 15:00"
}
```

---

## ✅ What it does

- Add events with unique IDs
- List events sorted by `start_time`
- Update existing events
- Delete events
- Store all data in `events.json` (human-readable & portable)

---
## 🧰 Quick overview

- `app.py`: defines API routes and logic
- `storage.py`: utility functions to read/write JSON data
- `events.json`: keeps your events data

---

## 📌 Requirements

- Python 3.7+
- Flask (installed via requirements.txt)

---
