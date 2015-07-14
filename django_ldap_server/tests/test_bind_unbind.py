from django.utils import unittest

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
        This tests if server works correctly if ANONYMOUS_SEARCH_ALLOWED is
        True

        Test procedure:
            - explicit enable ANONYMOUS_SEARCH_ALLOWED
            - send a search request
            - validate response contains result
            - reset ANONYMOUS_SEARCH_ALLOWED
        """
        pass

    def test_anonymous_disallowed(self):
        """
        This tests if server blocks correctly if ANONYMOUS_SEARCH_ALLOWED is
        False

        Test procedure:
            - explicit disable ANONYMOUS_SEARCH_ALLOWED
            - send a search request
            - validate response contains error message
            - reset ANONYMOUS_SEARCH_ALLOWED
        """
        pass

    def test_with_account_anonymous_allowed(self):
        """
        This tests if server works correctly if ANONYMOUS_SEARCH_ALLOWED is
        True. As this setting should not interfer with bind requests providing
        credentials, simply __test_with_account is called

        Test procedure:
            - explicit enable ANONYMOUS_SEARCH_ALLOWED
            - call helper function
            - reset ANONYMOUS_SEARCH_ALLOWED
        """
        self.__test_with_account()

    def test_with_account_anonymous_disallowed(self):
        """
        This tests if server works correctly if ANONYMOUS_SEARCH_ALLOWED is
        False. As this setting should not interfer with bind requests providing
        credentials, simply __test_with_account is called

        Test procedure:
            - explicit disable ANONYMOUS_SEARCH_ALLOWED
            - call helper function
            - reset ANONYMOUS_SEARCH_ALLOWED
        """
        self.__test_with_account()

    def __test_with_account(self):
        """
        Helper function for testing bind requests with credentials as this
        request should behave indepently from ANONYMOUS_SEARCH_ALLOWED

        Test procedure:
            - send bind request
            - validate response contains success code
            - send search request
            - validate response contains result
            - send unbind request
            - validate response contains success code
        """
        pass
