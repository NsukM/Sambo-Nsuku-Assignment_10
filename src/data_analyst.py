class DataAnalyst:
    def _init_(self, analyst_id, name, access_level):
        self.analyst_id = analyst_id
        self.name = name
        self.access_level = access_level

    def review_stat(self):
        return "Stat reviewed."

    def manage_reports(self):
        return "Reports managed."


