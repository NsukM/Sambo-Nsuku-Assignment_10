class ActivitySession:
    def _init_(self, session_id, date, duration, steps, calories):
        self.session_id = session_id
        self.date = date
        self.duration = duration
        self.steps = steps
        self.calories = calories

    def start_session(self):
        return "Session started."

    def end_session(self):
        return "Session ended."

    def sync(self):
        return "Session synced."


