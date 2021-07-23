import os
import sys
import readline
import glob

# i take this script from spooky (:

commands = ["use handshake/encryption/all", "use handshake/encryption/wep",
"use handshake/encryption/wpa", "use sniff/my/device",
"use network/scan/devices", "use port/scan",
"use fake/wifi", "use password/wifi",
"use deauth/attack/wifi/aireplay-ng", "use deauth/attack/wifi/mdk3",
"use deauth/attack/wifi/one/device/aireplay-ng", "use arp/spoofing/attack",
"help", "clear",
"exit", "banner",
"use mac/spoofing/attack", "use fake/wifi/random"]


def completer(text, state):
    """
    complete commands from the list above
    """
    options = [i for i in commands if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

def pathCompleter(text,state):
    """
    This is the tab completer for systems paths.
    """
    if '~' in text:
        text = os.path.expanduser('~')
    if os.path.isdir(text):
        text += '/'
    return [x for x in glob.glob(text + '*')][state]

readline.set_completer_delims('\t')
readline.parse_and_bind("tab: complete")

def PathComplete():
    readline.set_completer(pathCompleter)

def CommandComplete():
    readline.set_completer(completer)

def HistoryClear():
    readline.clear_history()