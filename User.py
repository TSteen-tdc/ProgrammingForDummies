class User:
    hello = ""
    goodbye = "And goodbye"

    def __init__(self, name):
        self.evaluate_name(name)

    def evaluate_name(self, name):
        self.hello = "Hello " + name
