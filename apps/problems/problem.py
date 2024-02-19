import problemTypes


class Problem:
    def __init__(self, name_of_problem: str, problemType: problemTypes.ProblemTypes):
        self._name_of_problem = name_of_problem.lower()
        self._problem = problemType

    def get_name(self):
        return self._name_of_problem

    def get_problem_name(self):
        return self._problem.value()


