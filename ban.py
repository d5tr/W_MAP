import random
from colorama import Fore


def bans():
    lst = [Fore.RED+'''
'
'              a8888b.
'             d888888b.
'             8P"YP"Y88
'             8|o||o|88      INSTA --> @d_5tr
'             8'    .88      TEAM --> @zer0one_01 
'             8`._.' Y8.
'            d/      `8b.
'           dP   .    Y8b.
'          d8:'  "  `::88b
'         d8"         'Y88b    I think linux is the best os (:
'        :8P    '      :888
'         8a.   :     _a88P
'       ._/"Yaa_:   .| 88P|
'       \    YP"    `| 8P  `.
'       /     \.___.d|    .'
'       `--..__)8888P`._.'
'
'        [1] Handshake ALL
'        [2] Sniff
'        [3] Know ip with you
'        [4] Port scan 
'        [5] Fake wifi
'        [6] Handshake WEP only
'        [7] Handshake WPA only 
'        [99] exit
    
    ''', Fore.LIGHTWHITE_EX+'''
    '  ______________________________
     / \                             \.
    |   |                            |.
     \_ |                            |.
        |                            |.
        |                            |.
        |   INSTA-->@d_5tr           |.
        |                            |.
        |    TEAM-->zer0one_01       |.
        |                            |.
        |    NETWORK THE BEST FIELD  |.
        |                            |.
        |     don't use tool for     |.
        |     Illegal things         |.
        |                            |.
        |   _________________________|___
        |  /                            /.
        \_/____________________________/.
    
    
        [1] Handshake ALL
        [2] Sniff
        [3] Know ip with you
        [4] Port scan 
        [5] Fake wifi
        [6] Handshake WEP only
        [7] Handshake WPA only 
        [99] exit
    ''',Fore.LIGHTGREEN_EX+'''
                     _
                       | \
                       | |
                       | |
  |\                   | |
 /, ~\                / /
X     `-.....-------./ /
 ~-. ~  ~              | INSTA--> @d_5tr
    \             /    | TEAM--> @zer0one_01
     \  /_     ___\   /  
     | /\ ~~~~~   \ |          [ Did you follow me in Github ? ](https://github.com/d5tr)
     | | \        || |
     | |\ \       || )
    (_/ (_/      ((_/
    
        [1] Handshake ALL
        [2] Sniff
        [3] Know ip with you
        [4] Port scan 
        [5] Fake wifi
        [6] Handshake WEP only
        [7] Handshake WPA only 
        [99] exit
    
    ''',Fore.GREEN+'''
'                       .
'                       M
'                      dM
'                      MMr
'                     4MMML                  .
'                     MMMMM.                xf
'     .              "MMMMM               .MM-
'      Mh..          +MMMMMM            .MMMM
'      .MMM.         .MMMMML.          MMMMMh
'       )MMMh.        MMMMMM         MMMMMMM
'        3MMMMx.     'MMMMMMf      xnMMMMMM"      INSTA --->@d_5tr
'        '*MMMMM      MMMMMM.     nMMMMMMP"       TEAM --->@zer0one_01
'          *MMMMMx    "MMMMM\    .MMMMMMM=
'           *MMMMMh   "MMMMM"   JMMMMMMP
'             MMMMMM   3MMMM.  dMMMMMM            .
'              MMMMMM  "MMMM  .MMMMM(        .nnMP"
'  =..          *MMMMx  MMM"  dMMMM"    .nnMMMMM*          Programming like smoking weed !!
'    "MMn...     'MMMMr 'MM   MMM"   .nMMMMMMM*"        
'     "4MMMMnn..   *MMM  MM  MMP"  .dMMMMMMM""
'       ^MMMMMMMMx.  *ML "M .M*  .MMMMMM**"               
'          *PMMMMMMhn. *x > M  .MMMM**""
'             ""**MMMMhx/.h/ .=*"
'                      .3P"%....
'                    nP"     "*MMnx   
'    
'            [1] Handshake ALL
'            [2] Sniff
'            [3] Know ip with you
'            [4] Port scan 
'            [5] Fake wifi
'            [6] Handshake WEP only
'            [7] Handshake WPA only 
'            [99] exit
    
    ''',Fore.LIGHTBLUE_EX+'''
'                  ,_   .  ._. _.  .
'           , _-','|~\~      ~/      ;-'_   _-'     ,;_;_,    ~~-
'  /~~-\_/-'~'--' \~~| ',    ,'      /  / ~|-_\_/~/~      ~~--~~~~'--_
'  /              ,/'-/~ '\ ,' _  , '|,'|~                   ._/-, /~
'  ~/-'~\_,       '-,| '|. '   ~  ,\ /'~                /    /_  /~         INSTA --> @d_5tr
'.-~      '|        '',\~|\       _\~     ,_  ,               /|            TEAM --> @zer0one_01
'          '\        /'~          |_/~//,-,~  \ "         ,_,/ |
'           |       /            ._-~'\_ _~|              \ ) /
'            \   __-\           '/      ~ |\  \_          /  ~
'  .,         '\ |,  ~-_      - |          //_' ~|  /\  \~ ,             with d5tr you can hack the world !!
'               ~-_'  _;       '\           '-,   \,' /\/  |                    Follow him in instagram & telegram & github !!
'                '\_,~'\_       \_ _,       /'    '  |, /|'                Enjoy to hack the world ...
'                   /     \_       ~ |      /         \  ~'; -,_.
'                   |       ~\        |    |  ,        '-_, ,; ~ ~\
'                    \,      /        \    / /|            ,-, ,   -,
'                     |    ,/          |  |' |/          ,-   ~ \   '.
'                    ,|   ,/           \ ,/              \       |
'                    /    |             ~                 -~~-, /   _
'                    |  ,-'                                    ~    /
'                    / ,'                                      ~
'                    ',|  ~
'                      ~'
'                [1] Handshake ALL
'                [2] Sniff
'                [3] Know ip with you
'                [4] Port scan 
'                [5] Fake wifi
'                [6] Handshake WEP only
'                [7] Handshake WPA only 
'                [99] exit    
    ''']
    x = random.choices(lst)
    for i in x :
        i= str(i).strip()
        print(i)
