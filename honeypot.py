import sys
import argparse
from socket import socket, AF_INET, SOCK_STREAM

VERSION = '0.1'
welcome = b"Ubuntu 18.06 LTS\nserver login:"

def send_email(src_address):
    """ TODO: send an email if we're scanned / probed on this port """
    pass

def honeypot(address, port=23):
    """ created a single Threaded telnet listen port """
    try:
        ski = socket(AF_INET, SOCK_STREAM)
        ski.bind((address, port))
        ski.listen()

        conn,addr = ski.accept()

        print('Hoynepot has been visited by ' + addr[0])
        send_email(addr[0])
        conn.sendall(welcome)

        while True:
            data = conn.recv(1024)

            if data == b'\r\n':
                ski.close()
                sys.exit()

    except:
        ski.close()
        sys.exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Honeypot prototype',
        epilog='Version: ' + str(VERSION))
    parser.add_argument('-a', '--address', help='server ip address to use', action='store', required=True)
    args = parser.parse_args()

    honeypot(args.address)