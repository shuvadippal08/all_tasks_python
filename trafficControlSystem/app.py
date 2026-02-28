from Signals.city_signal import CitySignals
from Signals.highway_signal import HighwaySignals
from Controller.controller import SignalController
from app_logger import logger


logger.info(f"Traffic Simulation Started....")

controller = SignalController()
no_vehicle = int(input("Enter the number of vehicle:  "))

city_signal = CitySignals(no_vehicle)

highway_signal = HighwaySignals(no_vehicle)

controller.operate(city_signal)
controller.operate(highway_signal)
logger.info(f"")
