import time
import requests

def login(email, password):
    # TODO
    time.sleep(1)
    if email == 'adwaitbhope@gmail.com' and password == 'abc':
        return { 'name': 'Adwait Bhope', 'email': email, 'password': password }   # Return user object

    return False


def reset_password(user, old_password, new_password):
    # TODO
    time.sleep(1.5)
    if old_password != user['password']:
        return False, 'current password is incorrect'

    return True, ''


def search(user, query):
    # TODO
    time.sleep(0.5)
    return [{
            'store': 'Walmart',
            'name': 'Potatoes',
            'price': 4.99
        }, {
            'store': 'ALDI',
            'name': 'Potatoes',
            'price': 3.99
        }
    ]


def get_cart(user):
    # TODO
    time.sleep(0.5)
    return [{
            'name': 'Potatoes',
            'url': 'walmart.com/potatoes',
            'price': 4.99
        }
    ]
