#!/bin/sh
# ---------------------------------------#
#       ||P0rt F0x coded by Pr0xy F0x|| #
# ---------------------------------------#
import time
import socket
import colorama
from ping3 import ping
from termcolor import colored

# Function to Display ByeBye MSSG.
def byebye():
    print(), print(colored('Thanks for using my Port Scanner :)', 'blue'))
    print(), print(colored('<3', 'red'), (colored('Ethical Hacking and stay Legal ;)', 'green')))
    print(), print(colored('Pr0xy F0x', 'magenta'))


# Function for PORTSCAN.
def port_scanner(host, port):
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if mySocket.connect_ex((host, port)):
        print(colored("Host {0} Port {1} is Closed =(".format(host, port), 'red'))
    else:
        print(colored("Host {0} Port {1} is Open ^_^".format(host, port), 'green'))
        mySocket.close()


# Function Print Instruction at start
def instruct_me():
    print(colored('INSTRUCTION', 'magenta'))
    print(colored("type 'h' or 'host' your.host.name' to set host", 'green'))
    print(colored("type 'p' or 'port'  22,80,443' to set ports", 'yellow'))
    print(colored("type 's' or 'scan' to start scanning, use with --log to create a logfile", 'blue'))
    print(colored("type 'help' for help", 'white'))
    print(colored("type 'q' 'x' or 'exit' to exit", 'red'))
    print()
    print()


# Function Print Help
def help_me():
    print(colored('HELP', 'magenta'))
    print(colored("type 'h' or 'host' your.host.name' to change host", 'green'))
    print(colored("type 'p' or 'port'  22,80,443' to change ports", 'yellow'))
    print(colored("type 's' or 'scan' to start scanning, use with --log to create a logfile", 'blue'))
    print(colored("type 'q' 'x' or 'exit' to exit", 'red'))
    print()
    print()


# Function Print if empty
def if_empty():
    print()
    print(colored("Can't be empty", 'red'))
    print()

# A List of Items
items = list(range(0, 57))
l = len(items)

colorama.init()
print(colored(" ____       __          __        ____       __            ", "magenta"))
print(colored("/\\  _`\\   /'__`\\       /\\ \\__    /\\  _`\\   /'__`\\          ", "magenta"))
print(colored("\\ \\ \\L\\ \\/\\ \\/\\ \\  _ __\\ \\ ,_\\   \\ \\ \\L\\_\\/\\ \\/\\ \\  __  _  ", "magenta"))
print(colored(" \\ \\ ,__/\\ \\ \\ \\ \\/\\`'__\\ \\ \\/    \\ \\  _\\/\\ \\ \\ \\ \\/\\ \\/'\\ ", "magenta"))
print(colored("  \\ \\ \\/  \\ \\ \\_\\ \\ \\ \\/ \\ \\ \\_    \\ \\ \\/  \\ \\ \\_\\ \\/>  </ ", "magenta"))
print(colored("   \\ \\_\\   \\ \\____/\\ \\_\\  \\ \\__\\    \\ \\_\\   \\ \\____//\\_/\\_\\", "magenta"))
print(colored("    \\/_/    \\/___/  \\/_/   \\/__/     \\/_/    \\/___/ \\//\\/_/", "magenta") + colored(
    " | V. 0.1.0 Alpha", 'magenta'))
print()
print(colored("Coded by Pr0xy F0x: ", 'magenta'))
print(colored("GitHub: ", 'magenta') + (colored('https://github.com/Pr0xy-F0x', 'green')))

print()
print()
instruct_me()
host = ""
ports = []
while True:
    print('Current settings.')
    print('Host: {0}'.format('none' if host == '' else host))
    print('Ports: {0}'.format('none' if len(ports) == 0 else ','.join(map(str, ports))))
    user_input = input('> ')
    if user_input == "help":
        help_me()
    if user_input == "" or user_input == "h ":
        if_empty()
    elif user_input[:2] == "h ":
        host = user_input[2:]
        try:
            if not ping(host, timeout=5):
                print(colored("Host not answering to 'Ping' could be down?", 'red'))
        except PermissionError:
            print(colored("Unable to Ping without root permission please run as root!!", 'red'))
    elif user_input[:5] == "host ":
        host = user_input[5:]
        try:
            if not ping(host, timeout=5):
                print(colored("Host not answering to 'Ping' could be down?", 'red'))
        except PermissionError:
            print(colored("Unable to Ping without root permission please run as root!!", 'red'))
    elif user_input[:2] == "p ":
        ports = list(map(int, user_input[2:].split(",")))
    elif user_input[:5] == "port ":
        ports = list(map(int, user_input[5:].split(",")))
    elif user_input == "s" or user_input == "scan":
        print(colored("Starting Scan", 'green'))
        time.sleep(3)
        print()
        for port in ports:
            print(colored("Scanning Port {0}".format(port), 'blue'))
            port_scanner(host, port)
    elif user_input == 'e' or user_input == 'q' or user_input == 'exit':
        break

byebye()