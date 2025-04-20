
class DatabaseConnection:
    __instance = None

    def _new_(cls):
        if cls.__instance is None:
            cls._instance = super(DatabaseConnection, cls).new_(cls)
            cls.__instance.connected = False
        return cls.__instance

    def connect(self):
        self.connected = True
        return "Connected to DB"

    def disconnect(self):
        self.connected = False
        return "Disconnected"

