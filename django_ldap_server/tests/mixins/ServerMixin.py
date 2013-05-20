from django_ldap_server import app_settings
from django_ldap_server.server import LDAPServer

from gevent.server import StreamServer

class ServerMixin(object):
    """
    Helper class for tests.
    """
    def setUp(self):
        self.server = StreamServer((app_settings.BIND_IP, app_settings.BIND_PORT), LDAPServer())
        self.server.start()

    def tearDown(self):
        self.server.stop()
