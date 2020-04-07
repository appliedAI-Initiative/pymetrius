import json
import logging.handlers
import os

from typing import List, Union, Dict


log = logging.getLogger(__name__)

__config_instance = None

source_path = os.path.dirname(__file__)


class __Configuration:
    """
    Holds essential configuration entries
    """
    log = log.getChild(__qualname__)

    def __init__(self, config_files: List[str] = None):
        """
        :param config_files: list of JSON configuration files (relative to root) from which to read.
            If None, reads from './config.json' and './config_local.json' (latter files have precedence)
        """
        if config_files is None:
            config_files = ["config.json", "config_local.json"]
        self.config = {}
        for filename in config_files:
            file_path = os.path.join(source_path, filename)
            if os.path.exists(file_path):
                self.log.info("Reading configuration from %s" % file_path)
                with open(file_path, 'r') as f:
                    self.config.update(json.load(f))
        if not self.config:
            raise Exception("No configuration entries could be read from %s" % config_files)

    def _get_non_empty_entry(self, key: Union[str, List[str]]) -> Union[float, str, List, Dict]:
        """
        Retrieves an entry from the configuration

        :param key: key or list of keys to go through hierarchically
        :return: the queried json object
        """
        if isinstance(key, str):
            key = [key]
        value = self.config
        for k in key:
            value = value.get(k)
            if value is None:
                raise Exception(f"Value for key '{key}' not set in configuration")
        return value

    def _get_path(self, key: Union[str, List[str]], create=False) -> str:
        """
        Retrieves an existing local path from the configuration

        :param key: key or list of keys to go through hierarchically
        :param create: if True, a directory with the given path will be created on the fly.
        :return: the queried path
        """
        path_string = self._get_non_empty_entry(key)
        path = os.path.abspath(path_string)
        if not os.path.exists(path):
            if isinstance(key, list):
                key = ".".join(key)  # purely for logging
            if create:
                log.info(f"Configured directory {key}='{path}' not found; will create it")
                os.makedirs(path)
            else:
                raise FileNotFoundError(f"Configured directory {key}='{path}' does not exist.")
        return path.replace("/", os.sep)


def get_config(reload=False) -> __Configuration:
    """
    :param reload: if True, the configuration will be reloaded from the json files
    :return: the configuration instance
    """
    global __config_instance
    if __config_instance is None or reload:
        __config_instance = __Configuration()
    return __config_instance
