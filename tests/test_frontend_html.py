import mock

from django.test import Client
from django.test import RequestFactory, TestCase

from frontend.views import homepage


class frontend_html_is_properly_rendered(TestCase):

    def test_frontend_returns_html(self):
        http_call = Client()
        response = http_call.get('/')

        look_text_in_response = 'Go'

        self.assertContains(response, look_text_in_response,
                            count=None, status_code=200, msg_prefix='',
                            html=False)

    def test_admin_site_is_disabled(self):
        response = self.client.get('/admin')
        self.assertEqual(response.status_code, 404)

    @mock.patch('frontend.views.environment_choice_form.radio_buttons_list', return_value=[])
    def test_frontend_raise_error_when_no_accounts_in_config(self, mocked_accounts):

        request = RequestFactory().get('/')

        response = homepage(request)

        look_text_in_response = 'No accounts found in configuration file'

        self.assertContains(response, look_text_in_response,
                            count=None, status_code=200, msg_prefix='',
                            html=False)

    def test_frontend_raise_error_when_aws_not_reachable(self):
        request_data = {'cloud_accounts': 'AWS-Account-1'}

        request = RequestFactory().post('/', data=request_data)

        response = homepage(request)

        look_text_in_response = 'Problem occurred when querying'

        self.assertContains(response, look_text_in_response,
                            count=None, status_code=200, msg_prefix='',
                            html=False)
