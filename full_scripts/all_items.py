# all_items.py

from .user_request import UserRequest


def run(user_request, menu):
    for item in range(1, 10):
        UserRequest.append(menu[str(item)].info.center(40, '~'))
        menu[str(item)].run(user_request)

    with open('check_domain.txt', 'w') as writer:
        writer.writelines(UserRequest.data)
    print('Done!')

    # fot testing puprposes:
    # for each in UserRequest.data:
    #     print(each, end='')

    UserRequest.release()
    menu['0'].run()
