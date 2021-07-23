import socket
from colorama import Fore


def Port_scan(host):

    numberx = 0

    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((host, port))  # scan
        numberx = numberx + 1
        print(f'\r ports scan : {numberx}', end="")
        if result == 0:
            def non():
                print(f'{Fore.CYAN}------------------------------{Fore.WHITE}')

            name_port = socket.getservbyport(port)  # get name port
            print(f"[{Fore.GREEN}+{Fore.WHITE}] Port {port} / {name_port} Open ")
            non()