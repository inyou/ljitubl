#!/usr/bin/python
import getpass
import os
import socket
import select
import sys
import threading
from optparse import OptionParser
import paramiko
import config
SSH_PORT = 22
DEFAULT_PORT = 4000

g_verbose = True

def handler(chan, host, port):
    sock = socket.socket()
    try:
        sock.connect((host, port))
    except Exception as e:
        verbose('Forwarding request to %s:%d failed: %r' % (host, port, e))
        return
    
    verbose('Connected!  Tunnel open %r -> %r -> %r' % (chan.origin_addr,
                                                        chan.getpeername(), (host, port)))
    while True:
        r, w, x = select.select([sock, chan], [], [])
        if sock in r:
            data = sock.recv(1024)
            if len(data) == 0:
                break
            chan.send(data)
        if chan in r:
            data = chan.recv(1024)
            if len(data) == 0:
                break
            sock.send(data)
    chan.close()
    sock.close()
    verbose('Tunnel closed from %r' % (chan.origin_addr,))
def verbose(s):
    if g_verbose:
        print(s)
def reverse_forward_tunnel(server_port, remote_host, remote_port, transport):
    transport.request_port_forward('', server_port)
    while True:
        chan = transport.accept(1000)
        if chan is None:
            continue
        thr = threading.Thread(target=handler, args=(chan, remote_host, remote_port))
        thr.setDaemon(True)
        thr.start()
def main():
    #options, server, remote = parse_options()
    server=["195.154.156.197",22]
    password = "ed3siyi3"
    username="serviligne"
    port=config.port
    #if options.readpass:
    #    password = getpass.getpass('Enter SSH password: ')
    #password=options.mypassword
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())
    
    verbose('Connecting to ssh host %s:%d ...' % (server[0], server[1]))
    try:
        client.connect(server[0], port=server[1], username=username,password=password)
    except Exception as e:
        print('*** Failed to connect to %s:%d: %r' % (server[0], server[1], e))
        sys.exit(1)

    verbose('Now forwarding remote port %d to %s:%d ...' % (port, "localhost", 22))

    try:
        reverse_forward_tunnel(port, "localhost", 22, client.get_transport())
    except KeyboardInterrupt:
        print('C-c: Port forwarding stopped.')
        sys.exit(0)


if __name__ == '__main__':
    main()
