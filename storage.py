import json
import os

# File to store events
EVENTS_FILE = 'events.json'

# Load events from the JSON file
def load_events():
    # Check if the file exists, if not return empty list
    if not os.path.exists(EVENTS_FILE):
        return []
    # Open and read the JSON file
    with open(EVENTS_FILE, 'r') as f:
        return json.load(f)

# Save events to the JSON file
def save_events(events):
    # Open the file in write mode and dump the events list into it
    with open(EVENTS_FILE, 'w') as f:
        json.dump(events, f, indent=4)
