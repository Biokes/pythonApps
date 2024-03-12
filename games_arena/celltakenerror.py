class CellTakenError(BaseException):

    def __init__(self):
        super().__init__("Cell taken, pls play elsewhere.")
