from Signals.base_signal import TrafficSignals
from app_logger import logger
from config import (
    CITY_SIGNAL_TRAFFIC_LIMIT,
    CITY_LOW_GREEN_TIME,
    CITY_HIGH_GREEN_TIME
)

class CitySignals(TrafficSignals):
    def greentime(self):
        logger.info(f"Calculating green time for City signal")
        if self._vehicle_count < CITY_SIGNAL_TRAFFIC_LIMIT:
            return CITY_LOW_GREEN_TIME
        return CITY_HIGH_GREEN_TIME
    
    def signal_type(self):
        return "City Signal"