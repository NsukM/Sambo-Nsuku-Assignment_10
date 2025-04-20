from abc import ABC, abstractmethod

class Recommendation(ABC):
    @abstractmethod
    def generate(self):
        pass

class SleepRecommendation(Recommendation):
    def generate(self):
        return "You need 8 hours of sleep tonight."

class ActivityRecommendation(Recommendation):
    def generate(self):
        return "Try walking 10,000 steps today."

class RecommendationGenerator(ABC):
    @abstractmethod
    def create_recommendation(self):
        pass

class SleepRecGenerator(RecommendationGenerator):
    def create_recommendation(self):
        return SleepRecommendation()

class ActivityRecGenerator(RecommendationGenerator):
    def create_recommendation(self):
        return ActivityRecommendation()


