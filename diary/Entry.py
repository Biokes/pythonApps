from datetime import date


class Entry:
    num = 100100
    def __init__(self, title: str, body: str,):
        self.body = body
        self.id = num + 1
        self.title = title
        self.dateCreated = date.today()

    def setTitle(self, title: str):
        self.title = title
        pass

    def getTitle(self):
        return self.title

    def getDate(self):
        return self.dateCreated

    def setBody(self, title: str):
        self.title = title
        pass

    def __str__(self):
        return f"idNumber : {self.id}\nTitle : {self.title}\nDate Created : {self.dateCreated}"
