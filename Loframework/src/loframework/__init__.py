
from .internal.driver import Driver
from loguru import logger
from .constres import DRIVERS,ADAPTERS

def run(driver:Driver=None,**kwargs):
  logger.info("Starting Loframework")
  if driver is None:
    raise Exception("Driver not loaded")
  logger.success(f"Driver:{driver} loaded")
  driver.run()
  
def load_driver(driver_name:str=None)->Driver:
  if driver_name is None:
    driver_name = 'asyncio'
  driver = DRIVERS[driver_name](ADAPTERS)
  logger.info(f"Loading driver: {driver_name}" )
  return driver

  
  
  
 