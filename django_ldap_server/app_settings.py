from django.conf import settings

BIND_IP = getattr(settings, 'LDAP_SERVER_BIND_IP', '127.0.0.1')
BIND_PORT = getattr(settings, 'LDAP_SERVER_BIND_PORT', 3389)

ANONYMOUS_SEARCH_ALLOWED = getattr(settings, 'LDAP_SERVER_ANONYMOUS_SEARCH_ALLOWED', False)
