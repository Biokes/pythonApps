from apps.class_examples.invalidnumbererror import InvalidNumberError


class Segments:

    def is_on(self, name: str):
        if name[7] == '1':
            return True
        return False

    def is_valid(self, numbers_given: str):
        if len(numbers_given) != 8 or not numbers_given.isnumeric():
            raise InvalidNumberError
        for items in numbers_given:
            if items not in ('0', '1'):
                raise InvalidNumberError
        return True

    def get_shape_of_index_one_and_five(self, numbers: str):
        if self.is_valid(numbers):
            if numbers[1] == numbers[5] == "1":
                alphabet = "#"
                return f"#{alphabet:>5}" + f"\n#{alphabet:>5}"
            if numbers[1] == numbers[5] == "0":
                alphabet = " "
                return f" {alphabet:>5}" + f"\n {alphabet:>5}"
            if numbers[1] == "1" and numbers[5] == "0":
                alphabet = "#"
                return f" {alphabet:>5}" + f"\n {alphabet:>5}"
            else:
                alphabet = " "
                return f"#{alphabet:>5}" + f"\n#{alphabet:>5}"

    def get_shape_of_index_two_and_four(self, numbers: str):
        if self.is_valid(numbers):
            if numbers[2] == numbers[4] == "1":
                alphabet = "#"
                return f"#{alphabet:>5}" + f"\n#{alphabet:>5}"
            if numbers[2] == numbers[4] == "0":
                alphabet = " "
                return f" {alphabet:>5}" + f"\n {alphabet:>5}"
            if numbers[2] == "1" and numbers[4] == "0":
                alphabet = "#"
                return f" {alphabet:>5}" + f"\n {alphabet:>5}"
            else:
                alphabet = " "
                return f"#{alphabet:>5}" + f"\n#{alphabet:>5}"

    def get_index_zero(self, numbers: str):
        if self.is_valid(numbers):
            if numbers[0] == "1":
                return f"{"#" * 6}"
            return f"{" " * 6}"

    def get_index_three(self, numbers: str):
        if self.is_valid(numbers):
            if numbers[3] == "1":
                return f"{"#" * 6}"
            return f"{" ":>6}"

    def get_index_seven(self, numbers: str):
        if self.is_valid(numbers):
            if numbers[6] == "1":
                return f"{"#" * 6}"
            return f"{" ":>6}"

    def get_shape(self, binary_digits):
        if self.is_on(binary_digits):
            return (f"{self.get_index_zero(binary_digits)}\n{self.get_shape_of_index_one_and_five(binary_digits)}"
                    f"\n{self.get_index_seven(binary_digits)}\n{self.get_shape_of_index_two_and_four(binary_digits)}" +
                    f"\n{self.get_index_three(binary_digits)}")
        return "   "

    def segments(self, binary_digits: str):
        print(self.get_shape(binary_digits))


if __name__ == '__main__':
    segment = Segments()
    number_given = "11011011"
    segment.segments(number_given)
