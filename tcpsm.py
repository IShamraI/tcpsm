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
    parser.add_argument("--port", default=-1, help="Target port")
    parser.add_argument("--start_port", default=-1, help="Start target port range to connect")
    parser.add_argument("--end_port", default=-1, help="End target port range to connect")

    args = parser.parse_args()
    sleep = int(args.sleep)
    count = int(args.count)
    port = int(args.port)
    start_port = int(args.start_port)
    end_port = int(args.end_port)
    host = args.host
    if port > 0:
        print("Creating {} connections to {}:{} and wait for {}".format(count, host, port, sleep))
        for i in range(count):
            threading.Thread(target=connect, args=(host, port, sleep,)).start()
    elif start_port > 0 and end_port > 0:
        for port in range(start_port, end_port):
            threading.Thread(target=connect, args=(host, port + 1, sleep,)).start()
    else:
        print("Unexpected set of params ...")
        return
    print("All connections are created. Sleep for {} seconds ...".format(sleep))
    time.sleep(sleep)
    print("Done. Bye ...")


if __name__ == "__main__":
    main()
