from flask import Flask, request, jsonify
from storage import load_events, save_events
import uuid  # To generate unique IDs for events
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Event Scheduler API! Try /events"

# Endpoint: Create a new event
@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()  # Get JSON data from request
    event = {
        "id": str(uuid.uuid4()),  # Generate unique ID
        "title": data.get("title"),
        "description": data.get("description"),
        "start_time": data.get("start_time"),  # Format: "YYYY-MM-DD HH:MM"
        "end_time": data.get("end_time")
    }
    events = load_events()  # Load existing events
    events.append(event)    # Add new event
    save_events(events)     # Save back to file
    return jsonify({"message": "Event created", "event": event}), 201

# Endpoint: List all events, sorted by start_time
@app.route('/events', methods=['GET'])
def list_events():
    events = load_events()
    # Sort events by start_time (earliest first)
    events.sort(key=lambda x: datetime.strptime(x["start_time"], "%Y-%m-%d %H:%M"))
    return jsonify(events)

# Endpoint: Update an existing event by its ID
@app.route('/events/<event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.get_json()  # Get new data from request
    events = load_events()
    for event in events:
        if event["id"] == event_id:
            # Update only provided fields, keep others unchanged
            event["title"] = data.get("title", event["title"])
            event["description"] = data.get("description", event["description"])
            event["start_time"] = data.get("start_time", event["start_time"])
            event["end_time"] = data.get("end_time", event["end_time"])
            save_events(events)  # Save updated events list
            return jsonify({"message": "Event updated", "event": event})
    return jsonify({"message": "Event not found"}), 404

# Endpoint: Delete an event by its ID
@app.route('/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    events = load_events()
    # Keep only events whose ID does not match
    events = [event for event in events if event["id"] != event_id]
    save_events(events)
    return jsonify({"message": "Event deleted"})

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for development
