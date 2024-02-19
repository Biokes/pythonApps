from problemTypes import ProblemTypes


class Person:
    problem_list = {}

    def __int__(self):
        self.problem_list = {}

    def add_problem(self, name: str, problem_name: ProblemTypes):
        name = name.lower()
        self.problem_list[name] = problem_name

    def re_count_problems(self) -> str:
        name = ''
        for elements in self.problem_list:
            name += elements.get_name() + " -> " + elements.get_Problem_type() + "\n"
        return name

    def solve_problem(self, name: str):
        name = name.lower()
        if name in self.problem_list:
            del self.problem_list[name]
        else:
            return ValueError("problem given does not exist in list")

    def size_of_problem_list(self) -> int:
        return len(self.problem_list)
