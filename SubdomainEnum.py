#!/usr/bin/python3
from dns.resolver import resolve, NoAnswer
import threading
from progressbar import ProgressBar
import argparse

#def get_input():
#    file_option = input(
#        "Select which file to use.\n(1) Small subdomain list\n(2) Medium subdomain list\n(3) Large subdomain list:  ")
#    if file_option == '1':
#        file_name = 'subdomains-small.txt'
#    elif file_option == '2':
#        file_name = 'subdomains-medium.txt'
#    elif file_option == '3':
#        file_name = 'subdomains-huge.txt'
#    else:
#        print('Invalid option.')
#        file_name = ""
#        get_input()
#    return file_name


def scan_domain(file_name, domain):
    pbar = ProgressBar()
    existing_urls = []
    with open(file_name, 'r') as file:
        name = file.read()
        sub_domains = name.splitlines()
    print(f'-----Scanning {domain} for {len(sub_domains)} subdomains-----')

    for subdomain in pbar(sub_domains):
        query = f"{subdomain}.{domain}"
        try:
            resolve(query, 'A')
            existing_urls.append(query)
        except:
            pass
    print(f'{len(existing_urls)} Subdomains found:')
    i = 0
    for i in existing_urls:
        print(f'[+] {i}')

try:
    parser = argparse.ArgumentParser(
            prog='',
            description='simple subdommain enumeration tool',
            add_help=True)

    parser.add_argument('-u', type=str, required=True, help="URL to scan")
    parser.add_argument('-w', type=str, required=True, help="Subdomain wordlist file")
    options = parser.parse_args()

    #domain = input('Enter the domain to scan: ').strip()
    #file_name = get_input()
    x = threading.Thread(target=scan_domain, args=(options.w, options.u,))
    x.start()

except KeyboardInterrupt:
    print("\nStopped by user")
