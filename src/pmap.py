import sys
from concurrent.futures import ThreadPoolExecutor

from general import get_my_nat_ip, parse_arguments, print_usage, get_subnet
from scan_network import send_icmp_packet


if __name__ == '__main__':
    args = parse_arguments()
    scan_network = getattr(args, 'scan_network')
    target_scan_host = getattr(args, 'scan_ports')
    target_flood_host = getattr(args, 'flood_host')

    if not (scan_network or target_scan_host or target_flood_host):
        print_usage()
        sys.exit()

    if scan_network:
        first, second, third = get_subnet(get_my_nat_ip())
        subnet = '.'.join([first, second, third]) + '.'
        with ThreadPoolExecutor(max_workers=64) as executor:
            jobs = []
            results_done = []

            for i in range(0, 256):
                target_ip = subnet + str(i)
                jobs.append(executor.submit(send_icmp_packet, (target_ip,)))

    if target_scan_host:
        print('he told me to scan target for ports')

    if target_flood_host:
        print('he told me to flood the target')
