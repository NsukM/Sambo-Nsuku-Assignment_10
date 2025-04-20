import copy

class Recommendation:
    def _init(self, rec_id, type, content, status="new"):
        self.rec_id = rec_id
        self.type = type_
        self.content = content
        self.status = status

    def clone(self):
        return copy.deepcopy(self)

class RecommendationCache:
    def _init_(self):
        self.cache = {}

    def add(self, key, recommendation):
        self.cache[key] = recommendation

    def get(self, key):
        return self.cache[key].clone()

