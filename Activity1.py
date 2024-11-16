# Base Class: Device
class Device:
    def __init__(self, brand, model, price):
        self._brand = brand
        self._model = model
        self._price = price

    def device_info(self):
        return f"Brand: {self._brand}, Model: {self._model}, Price: {self._price}"
    
# Subclass: Smartphone
class Smartphone(Device):
    def __init__(self, brand, model, price, os, storage, ram):
        super().__init__(brand, model, price)
        self._os = os
        self._storage = storage
        self._ram = ram
        self._apps =[]

    def install_app(self, app_name):
        self._apps.append(app_name)
        print(f"App '{app_name}' installed on {self._model}.")

    def remove_app(self, app_name):
        if app_name in self._apps:
            self._apps.remove(app_name)
            print(f"App '{app_name}' removed from {self._model}.")
        else:
            print(f"App '{app_name}' not found on {self._model}.")

    def list_apps(self):
        return f"Installed apps on {self._model}: {', '.join(self._apps) if self._apps else 'No apps installed.'}"
    
    def smartphone_info(self):
        return (f"{self.device_info()}, OS: {self._os}, Storage: {self._storage}GB, RAM: {self._ram}GB")
    
# Subclass: Gaming Smartphone (To demonstrate Polymorphism)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, os, storage, ram, cooling_system):
        super().__init__(brand, model, price, os, storage, ram)
        self._cooling_system = cooling_system
        self._game_mode = False
    
    def toggle_game_mode(self):
        self._game_mode = not self._game_mode
        state = "ON" if self._game_mode else "OFF"
        print(f"Game mode is now {state} on {self._model}")

    def smartphone_info(self):
        base_info = super().smartphone_info()
        return f"{base_info}, Cooling System: {self._cooling_system}"
    
# Example Usage
basic_phone = Smartphone("Samsung", "Galaxy S22", 999, "Android", 128, 8)
basic_phone.install_app("WhatsApp")
basic_phone.install_app("Spotify")
print(basic_phone.list_apps())
print(basic_phone.smartphone_info())

gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 1299, "Android", 512, 16, "Active Cooling")
gaming_phone.install_app("PUBG Mobile")
gaming_phone.toggle_game_mode()
print(gaming_phone.smartphone_info())


# EXPECTED OUTCOME
# App 'WhatsApp' installed on Galaxy S22.
# App 'Spotify' installed on Galaxy S22.
# Installed apps on Galaxy S22: WhatsApp, Spotify
# Brand: Samsung, Model: Galaxy S22, Price: 999, OS: Android, Storage: 128GB, RAM: 8GB
# App 'PUBG Mobile' installed on ROG Phone 6.
# Game mode is now ON on ROG Phone 6
# Brand: Asus, Model: ROG Phone 6, Price: 1299, OS: Android, Storage: 512GB, RAM: 16GB, Cooling System: Active Cooling