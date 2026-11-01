from .drivers.asyncio_driver import AsyncioDriver
from .adapters.console import ConsoleAdapter
DRIVERS = {
    "asyncio": AsyncioDriver
}
ADAPTERS = {
    "console": ConsoleAdapter
}