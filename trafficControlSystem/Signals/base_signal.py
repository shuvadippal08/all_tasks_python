from app_logger import logger
from abc import ABC, abstractmethod
class TrafficSignals(ABC):
    def __init__(self, vehicle_count:int)->None:
        self._vehicle_count = vehicle_count
        logger.info(f"Traffic signal created with vehicle count = {vehicle_count}")

    @abstractmethod
    def greentime(self):
        pass
    
    @abstractmethod
    def signal_type(self):
        pass