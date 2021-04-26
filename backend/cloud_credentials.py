import logging

from .config_file_parser import ConfigFileParser

logging.basicConfig(level="INFO")
log = logging.getLogger(__name__)


class CloudCredentials:

    def __init__(self):
        self.read_credentials_file()

        self.account_name = "not set"
        self.aws_login = "not_set"
        self.aws_pass = "not_set"
        self.aws_region = "not_set"

    def read_credentials_file(self):
        self.available_accounts = ConfigFileParser().account_list
        self.account_name_list = self.available_accounts.sections()

    def use_aws_credentials(self, cloud_account_name):
        config = self.available_accounts[cloud_account_name]

        log.info("Set credentials for account: %s", cloud_account_name)

        self.account_name = cloud_account_name

        if 'key_id' in config.keys():
            self.aws_login = config['key_id']
        if 'secret' in config.keys():
            self.aws_pass = config['secret']
        if 'region_name' in config.keys():
            self.aws_region = config['region_name']

        log.info("key_id: *******%s", self.aws_login[len(self.aws_login) - 3:])
        log.info("secret: ************")
        log.info("region: %s", self.aws_region)

        log.info("Set credentials complete")

    def get_cloud_account_list(self):
        return self.account_name_list
