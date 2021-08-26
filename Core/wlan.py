import netifaces
from Core.colors import *

def interfaces():
    x = netifaces.interfaces() # all interface

    print(f'[{Cyan}?{White}] Choose :')
    print('\n')
    for i in x:
        if i != 'lo': # we want interface without lo

            print(f' - {Green}{i}{White}')

    print('\n')



