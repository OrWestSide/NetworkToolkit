import os
import re
import socket
import argparse

ipRegex = re.compile(r'(\d{1,3}).(\d{1,3}).(\d{1,3}).\d{1,3}')


def parse_arguments():
    args = argparse.ArgumentParser()

    args.add_argument('-sn', '--scan-network',
                      help='Scan network for other devices',
                      action='store_true')
    args.add_argument('-sp', '--scan-ports',
                      help='Scan specified host for open ports',
                      type=str)
    args.add_argument('-fh', '--flood-host',
                      help='Constantly send packets to host in order to flood',
                      type=str)

    return args.parse_args()


def print_usage():
    os.system('python pmap.py -h')


def get_my_nat_ip():
    return socket.gethostbyname(socket.gethostname())


def get_subnet(host):
    return ipRegex.findall(host)[0]
