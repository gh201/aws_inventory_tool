from django.test import TestCase
from backend.config_file_parser import ConfigFileParser


class ConfigFileParser_test_case(TestCase):

    def test_configuration_parser_property_contains_accounts_info(self):
        application_configuration = ConfigFileParser()
        self.assertIsNotNone(application_configuration.account_list)
