class Recommendation:
    def _init(self, rec_id, type, content, status="new"):
        self.rec_id = rec_id
        self.type = type_
        self.content = content
        self.status = status

    def generate(self):
        return f"Recommendation generated: {self.content}"

    def accept(self):
        self.status = "accepted"

    def reject(self):
        self.status = "rejected"



