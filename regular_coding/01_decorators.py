
def my_decorator(func):
    def wrapper():
        print('This happens before mu function runs')

    return wrapper()

def is_logged_in(func):
    def wrapper():
        if USER_AUTHENTIFICATED:
            func()
        else:
            print('Cannot check balance, user is authenticated!')
    return wrapper()

@is_logged_in
def check_balance():
    print(3000)

USER_AUTHENTIFICATED = True
check_balance()



def check_balance():
    return 3000


current_balance = check_balance()
print(current_balance)

