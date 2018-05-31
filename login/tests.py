from django.test import TestCase

from login.service import ConnectionHandler
# Create your tests here.

class TestLoginService(TestCase):
    def test_connection_handler(self):
        try:
            detail = {
                'host': '172.16.1.10',
                'username': 'cisco',
                'password': 'cisco',
                'device_type': 'cisco_ios'
            }
            handler = ConnectionHandler(detail)
            handler.connect_router()
            self.assertTrue(handler.valid_router())
            handler.valid_router()
            handler.disconnect_router()
            self.assertFalse(handler.valid_router())
        except Exception as exception:
            print('error : ', exception)
