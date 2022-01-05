# About

`tcpsm` - tcp session manager. TCP load generator.

Do you need multiple tcp connections to test your app server? - Read examples :)

# Usage

    usage: tcpsm.py [-h] [--sleep SLEEP] [--count COUNT] [--host HOST] [--port PORT]
    
    optional arguments:
      -h, --help     show this help message and exit
      --sleep SLEEP  Exit after the specified amount of seconds and close all connections
      --count COUNT  Connections to keep open to the destinations
      --host HOST    Target host
      --port PORT    Target port

## TCP Examples
<details>
<summary>A few command line examples</summary>
Open 10000 connections to remote server and stop in 1 minute:

    tcpsm.py --count 10000 --host 192.168.1.1 --port 1000 --sleep 60

Open connections to remote server to ports from 1000 to 1100 and stop in 1 minute:

    tcpsm.py --host 192.168.1.1 --start_port 1000 --end_port 1100 --sleep 60

</details>
