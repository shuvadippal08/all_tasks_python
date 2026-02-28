from app_logger import logger

class SignalController:
    def operate(self,signal):
        logger.info(f"Signal Controller started for {signal.signal_type()}")
        time = signal.greentime()
        logger.info(f"{signal.signal_type()} --> Green for {time} seconds..")
        logger.info(f"Signal Controller operation Completed.")