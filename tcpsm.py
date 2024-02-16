#!/usr/bin/env python3
import argparse
import logging
import socket
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def connect(host, port, sleep, timeout):
    """
    Connect to the specified host and port, then sleep for the given duration.
    """
    try:
        with socket.socket(socket.AF_INET6 if ':' in host else socket.AF_INET) as sock:
            sock.settimeout(timeout)  # Set socket timeout
            sock.connect((host, port))
            time.sleep(sleep)
    except Exception as e:
        logging.error(f"Error connecting to {host}:{port}: {e}")

def main():
    """
    Main function to parse command line arguments and initiate connections.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--sleep", default=5, type=int, help="Exit after the specified amount of seconds and close all connections")
    parser.add_argument("--count", default=1, type=int, help="Connections to keep open to the destinations")
    parser.add_argument("--host", default='127.0.0.1', help="Target host")
    parser.add_argument("--port", default=-1, type=int, help="Target port")
    parser.add_argument("--start_port", default=-1, type=int, help="Start target port range to connect")
    parser.add_argument("--end_port", default=-1, type=int, help="End target port range to connect")
    parser.add_argument("--timeout", default=10, type=float, help="Timeout for socket connections")
    args = parser.parse_args()

    # Extract arguments
    sleep = args.sleep
    count = args.count
    host = args.host
    timeout = args.timeout

    # Check which mode to operate in
    if args.port > 0:
        port = args.port
        logging.info(f"Creating {count} connections to {host}:{port} and waiting for {sleep} seconds")
        with ThreadPoolExecutor(max_workers=count) as executor:
            for _ in range(count):
                executor.submit(connect, host, port, sleep, timeout)
    elif args.start_port > 0 and args.end_port > 0:
        start_port = args.start_port
        end_port = args.end_port
        logging.info(f"Creating connections to {host} ports {start_port}-{end_port} and waiting for {sleep} seconds")
        with ThreadPoolExecutor(max_workers=end_port - start_port) as executor:
            for port in range(start_port, end_port + 1):
                executor.submit(connect, host, port, sleep, timeout)
    else:
        logging.error("Unexpected set of params...")
        return

    logging.info(f"All connections are created. Sleeping for {sleep} seconds...")
    time.sleep(sleep)
    logging.info("Done. Bye...")

if __name__ == "__main__":
    main()
