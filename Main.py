from User import User


class Main:
    user = None

    def start(self):
        self.get_input()
        self.create_output()

    def get_input(self):
        print('Enter your name:')
        name = input()

        self.user = User(name)

    def create_output(self):
        print(self.user.hello)
        print(self.user.goodbye)
