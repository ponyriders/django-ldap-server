from django.utils import unittest

from django_ldap_server import app_settings
from django_ldap_server.tests.mixins.ServerMixin import ServerMixin

class BindUnbindTest(unittest.TestCase, ServerMixin):
    """ 
    Tests for the bind/unbind mechanism
    """

    def setUp(self):
        """
        Just calling super
        """
        super(BindUnbindTest, self).setUp()

    def tearDown(self):
        """
        Just calling super
        """
        super(BindUnbindTest, self).tearDown()

    def test_anonymous_allowed(self):
        """
        This tests if server works correctly if anonymous search is allowed
        """
        pass

    def test_anonymous_disallowed(self):
        """
        This tests if server blocks correctly if anonymous search is not allowed
        """
        pass

    def test_with_account_anonymous_allowed(self):
        """
        This tests if server works correctly if anonymous search is allowed.
        As this setting should not interfer with bind requests providing
        credentials, simply test_with_account_anonymous_disallowed is called 
        """
        self.test_anonymous_disallowed()

    def test_with_account_anonymous_disallowed(self):
        pass
