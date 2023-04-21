# frame.py
from dataclasses import dataclass
from inspect import getsourcefile
from os.path import abspath
from typing import Callable

from colorama import Fore as fg

import full_scripts.all_items as mod10
import full_scripts.get_soa as mod4
import full_scripts.host_ip as mod1
import full_scripts.mx_record as mod5
import full_scripts.reverse_dns as mod6
import full_scripts.reverse_ip as mod9
import full_scripts.robots as mod7
import full_scripts.site_location as mod2
import full_scripts.sitemap as mod8
import full_scripts.who_is as mod3
from full_scripts.user_request import UserRequest


@dataclass
class Menu:
    info: str
    run: Callable

    def __str__(self):
        return self.info


menu = {
    '0': Menu('Exit the program', exit),
    '1': Menu('Host IP', mod1.run),
    '2': Menu('Site location', mod2.run),
    '3': Menu('Whois', mod3.run),
    '4': Menu('Nslookup', mod4.run),
    '5': Menu('DNS MX-Record', mod5.run),
    '6': Menu('Reverse DNS', mod6.run),
    '7': Menu('robots.txt', mod7.run),
    '8': Menu('sitemap.xml', mod8.run),
    '9': Menu('Reverse ip lookup', mod9.run),
    '10': Menu('All items', mod10.run)
}


def print_menu():
    try:
        logo_path = abspath(getsourcefile(lambda: 0))
    except OSError:
        print('File "logo.txt" is missing')
        return
    try:
        with open(logo_path[:-8] + 'full_scripts/logo.txt', 'r') as logo:
            print(fg.GREEN + logo.read() + fg.RESET)
    except FileNotFoundError:
        print('File "logo.txt" is missing')
    header = '\n' + '\n'.join([f'{num}. {menu[num]}' for num in menu])
    print(header)


def get_user_input():
    while usr_input := input('\nEnter the option number: '):
        if usr_input not in menu.keys():
            print(fg.RED + 'User choice is incorrect' + fg.RESET)
            print_menu()
            continue
        elif usr_input == '0':
            break
        elif usr_input == '10':
            # for testing
            # req = UserRequest(test='https://fishki.net/')
            req = UserRequest()
            if req.isEmpty:
                print('User input required')
                continue
            menu[usr_input].run(req, menu)
        else:
            print(menu[usr_input].info.center(40, '~'))
            menu[usr_input].run()


def cli():
    """ Точка входа в приложение """
    print_menu()
    try:
        get_user_input()
    except KeyboardInterrupt:
        print('\nProgram terminated by user request')
        return


if __name__ == "__main__":
    cli()
