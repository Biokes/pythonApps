

class Drill:
    def __init__(self):
        self.word = ''

    def printString(self):
        return self.__str__()

    def get_string(self):
        self.word = input("Enter anything: ")

    def __str__(self):
        self.get_string()
        return self.word.upper()


drill = Drill()
print(drill.__str__())
