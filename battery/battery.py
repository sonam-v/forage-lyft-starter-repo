from abc import ABC

class Battery(ABC):

    def needs_service(self):
        pass

class SpindlerBattery(Battery):
    
    def __init__(self, last_service_date, current_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
    
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return service_threshold_date < self.current_date

class NubbinBattery(Battery):
    
    def __init__(self, last_service_date, current_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
    
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return service_threshold_date < self.current_date
