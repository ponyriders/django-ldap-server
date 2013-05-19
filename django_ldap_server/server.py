import logging

from django_ldap_server import app_settings

from gevent.server import StreamServer

from pyasn1.error import PyAsn1Error
from pyasn1_modules.rfc2251 import decoder, encoder, LDAPMessage, BindResponse


logging.basicConfig(level=logging.INFO)


class LDAPServer(object):
    """
    Class handling the ldap protocol.
    """
    logger = logging.getLogger('django_ldap_server')

    def __call__(self, socket, address):
        """
        New incoming connection
        """
        self.socket = socket
        self.address = address

        # while socket is open, read ldap messages from it and dispatch them to handlers
        while not self.socket.closed:
            self.dispatch_msg(self.recv_msg())

    def recv_msg(self):
        """
        reads a ldap message from socket and return it - else None
        """
        recv_buffer = ''
        while True:
            data = self.socket.recv(2 ** 10)
            if not data:
                return None
            recv_buffer += data

            try:
                msg, _ = decoder.decode(recv_buffer, asn1Spec=LDAPMessage())
                print recv_buffer
                return msg
            except PyAsn1Error:
                continue

    def __answer_msg(self, last_received_msg):
        """
        Helper to simply answer to a ldap request reusing the last received message.
        """
        def wrapped(operation):
            self.socket.send(encoder.encode(
                last_received_msg.setComponentByName('protocolOp', operation)
            ))
        return wrapped


    def dispatch_msg(self, msg):
        """
        Extracts the ldaop operation from ldap message and dispatches it to it's corresponding handler method
        """
        operation = msg.getComponentByName('protocolOp').getComponent()
        handler_name = 'handle_%s' % operation.__class__.__name__.lower()
        if hasattr(self, handler_name):
            getattr(self, handler_name)(operation, self.__answer_msg(msg))
        else:
            self.logger.warn('Operation not handled: %s', operation)

    def handle_bindrequest(self, operation, answer):
        """
        Handles a BindRequest. Used for authentication.
        """
        name = operation.getComponentByName('name')
        passwd = operation.getComponentByName('authentication').getComponentByPosition(0)

        # TODO: do the authentication here
        code, error_message = 0, ''

        answer(
            BindResponse()
            .setComponentByName('resultCode', code)
            .setComponentByName('matchedDN', '')
            .setComponentByName('errorMessage', error_message)
        )

    def handle_searchrequest(self, operation, answer):
        print operation


def main():
    print "Starting"
    StreamServer((app_settings.BIND_IP, app_settings.BIND_PORT), LDAPServer()).serve_forever()


if __name__ == '__main__':
    main()
