from app_logger import logger
from ABC import abstractclass
class TrafficSignals(ABC):
    def __init__(self, vehicle_count:int)->None:
        self.vehicle_count = vehicle_count
        logger.info(f"Traffic signal created with vehicle count = {vehicle_count}")

    @abstractclasss
    def greentime(self):
        pass

    def signal_type(self):
        pass