from django.test import TestCase

from backend.cloud_credentials import CloudCredentials


class CloudCredentials_tests(TestCase):

    def test_account_names_returned(self):
        result = CloudCredentials()
        accounts = result.get_cloud_account_list()

        self.assertIsNotNone(accounts)
        self.assertListEqual(accounts, ['AWS-Account-1', 'AWS-Account-2',
                                        'AWS-Account-3'])

    def test_credentials_set_correctly(self):
        result = CloudCredentials()
        result.use_aws_credentials('AWS-Account-1')

        self.assertEqual(result.aws_region, 'eu-west-1')
        self.assertEqual(result.aws_login, 'my_aws_account_key_id')
        self.assertEqual(result.aws_pass, 'my_aws_account_secret_string')
