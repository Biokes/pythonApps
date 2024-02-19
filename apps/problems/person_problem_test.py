import unittest
from apps.problems.Person import Person
from apps.problems.problemTypes import ProblemTypes


class MyTestCase(unittest.TestCase):

    def testThatPerson_can_add_to_his_problem_list(self):
        person: Person = Person()
        self.assertEqual(0, person.size_of_problem_list())
        person.add_problem("name", ProblemTypes.EDUCATION)
        self.assertEqual(1, person.size_of_problem_list())
        person.add_problem("Money", ProblemTypes.EDUCATION)
        self.assertEqual(2, person.size_of_problem_list())
        person.add_problem("no money", ProblemTypes.EDUCATION)
        self.assertEqual(3, person.size_of_problem_list())

    def testThatUserCanSolveProblem(self):
        person1: Person = Person()
        person1.add_problem("school fees", ProblemTypes.EDUCATION)
        person1.add_problem("Money", ProblemTypes.EDUCATION)
        self.assertEqual(2, person1.size_of_problem_list())
        person1.solve_problem("money")
        self.assertEqual(1, person1.size_of_problem_list())

