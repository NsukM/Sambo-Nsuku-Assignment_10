class FitnessProfile:
    def _init_(self, age, weight, height, activity_level):
        self.age = age
        self.weight = weight
        self.height = height
        self.activity_level = activity_level

    def calculate_bmi(self):
        return self.weight / ((self.height / 100) ** 2)

    def update_profile(self, age=None, weight=None, height=None, activity_level=None):
        if age: self.age = age
        if weight: self.weight = weight
        if height: self.height = height
        if activity_level: self.activity_level = activity_level


