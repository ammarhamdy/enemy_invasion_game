class EventHandler:
    def __init__(self):
        self.events = {}

    def add_event(self, event_type: int, event=lambda: None):
        self.events[event_type] = event

    def check_events(self, events_queue):
        for event in events_queue:
            self.events.get(event.type, lambda x: None)(event)
