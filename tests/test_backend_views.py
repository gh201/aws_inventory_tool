from django.test import TestCase

from backend.views import CloudReader
from backend.cloud_credentials import CloudCredentials


credentials = CloudCredentials()


class CloudReaderTests(TestCase):

    assets = CloudReader('AWS-Account-3')

    def test_get_compute_info_returns_data(self):
        self.assertIsNotNone(self.assets.get_compute_info())

    def test_get_elb_info_returns_data(self):
        self.assertIsNotNone(self.assets.get_loadbalancing_info())

    def test_get_dba_info_returns_data(self):
        self.assertIsNotNone(self.assets.get_database_info())

    def test_get_dns_info_returns_data(self):
        self.assertIsNotNone(self.assets.get_dns_info())

    def test_get_objectstore_info_returns_data(self):
        self.assertIsNotNone(self.assets.get_objectstore_info())
