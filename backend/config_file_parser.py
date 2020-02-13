import os
import logging

from configparser import ConfigParser

logging.basicConfig(level="INFO")
log = logging.getLogger(__name__)


class ConfigFileParser():

    def __init__(self):

        self.account_list = []
        self.config_file_name = 'config.ini'

        working_dir = os.path.dirname(os.path.realpath(__file__))
        config_file_path = os.path.join(working_dir, self.config_file_name)

        self._parse_config_file(config_file_path)

    def _parse_config_file(self, config_file_path):
        log.info("Reading config from %s", config_file_path)

        configuration_data = ConfigParser()
        configuration_data.read(config_file_path)

        self.account_list = configuration_data

        log.info("Found %s account details", len(self.account_list.sections()))
