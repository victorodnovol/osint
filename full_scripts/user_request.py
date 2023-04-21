# user_request.py

import re
import socket


class UserRequest:
    """ Класс для сбора и проверки данных пользователя """
    data = []
    isEmpty = True

    def __init__(self, empty=False, test=None):
        self.without_https = None
        self.with_https = None
        self.addr = None
        if UserRequest.isEmpty or test:
            self._get_input(test=test)

    def _get_input(self, test=None) -> None:
        """Функция проверяет ввод пользователя и получает IP"""
        if not test:
            user_input = input('\nEnter domain address [https://site.com]: ')
        else:
            user_input = test
        host = re.match(r'(https?://)((?!.*/{2})\w+\.\w{2,3})/?.*', user_input)
        # ip = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', user_input)
        if not host:
            print('The input provided is not valid')
            return False
        else:
            host = host.groups()
        try:
            self.addr = socket.gethostbyname(host[1])
        except socket.gaierror as e:
            print('Error: ', e)
            return
        self.with_https = host[0] + host[1]
        self.without_https = host[1]
        UserRequest.isEmpty = False

    @staticmethod
    def append(user_data: str) -> None:
        if not UserRequest.isEmpty and type(user_data) is str:
            UserRequest.data.append(user_data + '\n')
        else:
            print(user_data)

    @staticmethod
    def release() -> None:
        """ Очистить данные ввода пользователя """
        UserRequest.data.clear()
        UserRequest.isEmpty = True


if __name__ == "__main__":
    UserRequest()
