from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def generate(self): pass

class Summary(ABC):
    @abstractmethod
    def show(self): pass

class DailyReport(Report):
    def generate(self):
        return "Generated daily report."

class WeeklySummary(Summary):
    def show(self):
        return "Weekly summary shown."

class ReportFactory(ABC):
    @abstractmethod
    def create_report(self): pass
    @abstractmethod
    def create_summary(self): pass

class FitnessDataFactory(ReportFactory):
    def create_report(self):
        return DailyReport()

    def create_summary(self):
        return WeeklySummary()

