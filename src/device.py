class Device:
    def _init_(self, device_id, brand, model, is_connected=False):
        self.device_id = device_id
        self.brand = brand
        self.model = model
        self.is_connected = is_connected

    def connect(self):
        self.is_connected = True
        return "Device connected."

    def disconnect(self):
        self.is_connected = False
        return "Device disconnected."

    def sync_data(self):
        return "Data synced." if self.is_connected else "Connect device first."

