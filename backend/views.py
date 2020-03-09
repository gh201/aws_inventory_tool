import logging

from .cloud_reader_aws import ReaderAws
from .cloud_credentials import CloudCredentials

logging.basicConfig(level="INFO")
log = logging.getLogger(__name__)

credentials = CloudCredentials()


class CloudReader:

    def __init__(self, target_account_name):
        self._set_target_account(target_account_name)
        self.aws_info = ReaderAws(aws_credentials=credentials)

    def _set_target_account(self, target_account_name):
        credentials.use_aws_credentials(target_account_name)

    def get_compute_info(self):
        list = self.aws_info.get_ec2_instance_info()
        return list

    def get_loadbalancing_info(self):
        list = self.aws_info.get_elb_info()
        return list

    def get_database_info(self):
        list = self.aws_info.get_rds_info()
        return list

    def get_dns_info(self):
        list = self.aws_info.get_route53_info()
        return list

    def get_objectstore_info(self):
        list = self.aws_info.get_s3_info()
        return list


def get_available_account_names():
    return credentials.get_cloud_account_list()
