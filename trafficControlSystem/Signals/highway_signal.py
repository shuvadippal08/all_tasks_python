from Signals.base_signal import TrafficSignals
from app_logger import logger
from config import (
    HIGHWAY_SIGNAL_TRAFFIC_LIMIT,
    HIGHWAY_LOW_GREEN_TIME,
    HIGHWAY_HIGH_GREEN_TIME
)

class HighwaySignals(TrafficSignals):
    def greentime(self):
        logger.info(f"Calculating green time for Highway signal")
        if self._vehicle_count < HIGHWAY_SIGNAL_TRAFFIC_LIMIT:
            return HIGHWAY_LOW_GREEN_TIME
        return HIGHWAY_HIGH_GREEN_TIME
    
    def signal_type(self):
        return "Highway Signal"