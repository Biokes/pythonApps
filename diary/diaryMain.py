class DiaryMain:

    @staticmethod
    def validate(name: str):
        return len(name)

    @staticmethod
    def prompt():
        name: str = input("welcome\nEnter your name: ")
        password: str = input("enter preferred password: ")
        return [name, password]



