from __future__ import print_function

import time
import socket
import argparse
import threading


def connect(host, port, sleep):
    sock = socket.socket()
    sock.connect((host, port))
    time.sleep(sleep)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sleep", default=5, help="Exit after the specified amount of seconds and close all connections")
    parser.add_argument("--count", default=1, help="Connections to keep open to the destinations")
    parser.add_argument("--host", default='127.0.0.1', help="Target host")
    parser.add_argument("--port", default=3000, help="Target port")

    args = parser.parse_args()
    sleep = int(args.sleep)
    count = int(args.count)
    port = int(args.port)
    host = args.host
    print("Creating {} connections to {}:{} and wait for {}".format(count, host, port, sleep))
    for i in range(count):
        threading.Thread(target=connect, args=(host, port, sleep,)).start()

    print("All {} connections are created. Sleep for {} seconds ...".format(count, sleep))
    time.sleep(sleep)
    print("Done. Bye ...")


if __name__ == "__main__":
    main()
