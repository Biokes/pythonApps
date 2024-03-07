from apps.class_examples.invalidnumbererror import InvalidNumberError


class Logistics:
    @staticmethod
    def calculateWage(deliveries: int):
        if deliveries < 1:
            raise InvalidNumberError
        return Logistics.__deliveriesRate(deliveries) + 5000

    @staticmethod
    def __deliveriesRate(number_of_deliveries: int):
        return number_of_deliveries * 160
