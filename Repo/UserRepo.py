

class UserResult:
    name: str = None
    repeat: bool = False

    def __init__(self, name: str, repeat: bool):
        self.name = name
        self.repeat = repeat


class UserRepo:
    user_ids = {
        "Joe": 312,
        "Bob": 349,
        "Bill Clinton": 12,
        "Darth Vader": 19,
        "Dr who": 13,
        "John Mcclane": 15,
        "Nick Fury": 67,
        "Luke Skywalker": 17,
    }

    users = {
        12: UserResult("Bill Clinton", False),
        13: UserResult("Dr who", True),
        15: UserResult("John Mcclane", True),
        17: UserResult("Luke Skywalker", False),
        19: UserResult("Darth Vader", False),
        67: UserResult("Nick Fury", True),
        312: UserResult("Joe", False),
        349: UserResult("Bob", True)
    }

    def get_user_id(self, username: str, password: str) -> int:
        "Outputs the userid matching a certain username and password. If no userid matches the given input, the method returns -1."
        return self.user_ids.get(username, -1)

    def get_user(self, user_id: int) -> UserResult:
        "Outputs a DbUser object containing the data for the user matching the userid. If no user is found for the userid returns None."
        return self.users.get(user_id, None)
