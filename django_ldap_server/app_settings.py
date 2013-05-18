from django.conf import settings


ANONYMOUS_SEARCH_ALLOWED = getattr(settings, 'LDAP_SERVER_ANONYMOUS_SEARCH_ALLOWED', False)
