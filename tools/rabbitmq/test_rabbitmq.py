#!/usr/bin/env python
import socket
from kombu import Connection
host = "localhost"
port = 5672
user = "guest"
password = "guest"
vhost = "/"
url = 'amqp://{0}:{1}@{2}:{3}/{4}'.format(user, password, host, port, vhost)
with Connection(url) as c:
    try:
        c.connect()
    except socket.error:
        raise ValueError("Received socket.error, "
                         "rabbitmq server probably isn't running")
    except IOError:
        raise ValueError("Received IOError, probably bad credentials")
    else:
        print "Credentials are valid"
