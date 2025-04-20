class VitalStat:
    def _init_(self, stat_type, value):
        self.stat_type = stat_type
        self.value = value

class VitalStatFactory:
    @staticmethod
    def create_stat(stat_type, value):
        return VitalStat(stat_type, value)


