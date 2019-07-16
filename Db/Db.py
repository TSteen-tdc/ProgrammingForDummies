class DbUser:
    name: str = None
    repeat: bool = False

    def __init__(self, name: str, repeat: bool):
        self.name = name
        self.repeat = repeat


class Db:
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
        12: DbUser("Bill Clinton", False),
        13: DbUser("Dr who", True),
        15: DbUser("John Mcclane", True),
        17: DbUser("Luke Skywalker", False),
        19: DbUser("Darth Vader", False),
        67: DbUser("Nick Fury", True),
        312: DbUser("Joe", False),
        349: DbUser("Bob", True)
    }

    def get_user_id(self, username: str, password: str) -> int:
        return self.user_ids.get(username, -1)

    def get_user(self, user_id: int) -> DbUser:
        return self.users.get(user_id, None)
