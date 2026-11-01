from .matcher import Matcher
from loguru import logger
import tomllib
import importlib
import importlib.util

path:str=""
with open("Loframework/pyproject.toml","rb") as f:
    config = tomllib.load(f)
    # path = config["tool"]["losakura"]["matcher"]["test_matchers"][0]
    path = config["tool"]["losakura"]["matcher"]["matchers"][0]
    logger.debug(f"Matcher path: {path}")
try:
    if importlib.util.find_spec(path):
        importlib.import_module(path)
except ModuleNotFoundError:
    logger.error(f"Matcher path: {path} not found")

