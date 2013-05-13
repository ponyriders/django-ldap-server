import logging
from pyasn1.error import PyAsn1Error


logging.basicConfig(level=logging.INFO)

from gevent.server import StreamServer

from pyasn1_modules.rfc2251 import decoder, encoder, LDAPMessage, BindResponse, BindRequest


def valid_authentication(message):
    """
    :rtype: (resultCode, errorMessage)
    """
    bind_request = message.getComponentByName('protocolOp')[0]
    if not isinstance(bind_request, BindRequest):
        return 2, 'You shall send a BindRequest first'

    name = bind_request.getComponentByName('name')
    passwd = bind_request.getComponentByName('authentication').getComponentByPosition(0)

    # TODO: check id and authozization based on ldap
    return 0, ''


def recv_ldap_message(socket):
    """
    reads a ldap message from socket and return it - else None
    """
    buffer = ''
    while True:
        data = socket.recv(2 ** 10)
        if not data:
            return None
        buffer += data

        try:
            msg, _ = decoder.decode(buffer, asn1Spec=LDAPMessage())
            return msg
        except PyAsn1Error:
            continue


def handle(socket, address):
    print 'new connection!'

    bind_request = recv_ldap_message(socket)
    code, error_message = valid_authentication(bind_request)

    bound = code == 0

    socket.send(encoder.encode(
        bind_request.setComponentByName(
            'protocolOp',
            BindResponse()
            .setComponentByName('resultCode', code)
            .setComponentByName('matchedDN', '')
            .setComponentByName('errorMessage', error_message)
        )
    ))




    next = recv_ldap_message(socket)

    print next.prettyPrint()



def main():
    print "Starting"
    server = StreamServer(('127.0.0.1', 3389), handle)  # creates a new server
    server.serve_forever()


if __name__ == '__main__':
    main()