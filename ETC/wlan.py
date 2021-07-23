import netifaces
from colorama import Fore
def interfaces():
    x = netifaces.interfaces() # all interface

    print(f'[{Fore.CYAN}?{Fore.WHITE}] Choose :')
    print('\n')
    for i in x:
        if i != 'lo': # we want interface without lo

            print(f' - {Fore.GREEN}{i}{Fore.WHITE}')

    print('\n')



