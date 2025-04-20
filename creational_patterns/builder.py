class FitnessProfile:
    def _init_(self):
        self.age = None
        self.weight = None
        self.height = None
        self.activity_level = None

    def _str_(self):
        return f"Profile: {self.age}y, {self.weight}kg, {self.height}cm, {self.activity_level}"

class FitnessProfileBuilder:
    def _init_(self):
        self.profile = FitnessProfile()

    def set_age(self, age):
        self.profile.age = age
        return self

    def set_weight(self, weight):
        self.profile.weight = weight
        return self

    def set_height(self, height):
        self.profile.height = height
        return self

    def set_activity_level(self, level):
        self.profile.activity_level = level
        return self

    def build(self):
        return self.profile

