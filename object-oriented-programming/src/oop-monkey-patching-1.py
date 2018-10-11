class User:
    def hello(self):
        print('hello')


def monkey_patch():
    print('My function')


User.hello = monkey_patch
User.hello()
# 'My function'