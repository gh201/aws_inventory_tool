from django.test import RequestFactory, TestCase

from frontend.http_request_parser import get_client_ip


class HTTPRequestParserTest(TestCase):

    def test_client_ip_extracted(self):
        request = RequestFactory().get('/')

        client_ip = get_client_ip(request)

        self.assertEqual(client_ip, '127.0.0.1')
