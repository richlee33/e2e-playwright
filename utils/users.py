users = [
    {"name": "standard_user", "username": "standard_user", "password": "secret_sauce"},
    {"name": "locked_out_user", "username": "locked_out_user", "password": "secret_sauce"},
]

checkout_info = [
    {"name": "john", "first_name": "john", "last_name": "smith", "zip": "11101"},
    {"name": "mary", "first_name": "mary", "last_name": "jones", "zip": "99909"},
]

def get_user(name):
    try:
        return next(user for user in users if user["name"] == name)
    except StopIteration as e:
        print ("\nUser %s is not defined, enter a valid user.\n" %name)
        raise e

def get_checkout_info(name):
    try:
        return next(user for user in checkout_info if user["name"] == name)
    except StopIteration as e:
        print("\nCheckout user %s is not defined, enter a checkout user.\n" % name)
        raise e