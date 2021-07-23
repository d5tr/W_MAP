from colorama import Fore

def Make_file_for_wifi():
    while True:
        print(f'{Fore.RED}Type one name at a time{Fore.WHITE}')
        print(f'{Fore.RED}To stop writing network names{Fore.WHITE}')
        Names = input(f'\n[{Fore.CYAN}?{Fore.WHITE}]Enter name WI-FI : ')

