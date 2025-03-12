#!/usr/bin/env python3
import signal
import sys
from forwardshell import ForwardShell
from termcolor import colored


def def_hadler(sig, frame):
    print(colored(f"\n\n[+]Saliendo..\n", 'red'))
    my_forwardshell.remove_data()
    sys.exit(1)

signal.signal(signal.SIGINT, def_hadler)

if __name__ == '__main__':
    my_forwardshell = ForwardShell()
    my_forwardshell.run()
