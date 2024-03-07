from apps.class_examples.invalidnumbererror import InvalidNumberError


class Logistics:
    @staticmethod
    def calculateWage(deliveries: int):
        if deliveries < 0:
            raise InvalidNumberError
        return Logistics.__deliveriesRate(deliveries) + 5000

    @staticmethod
    def __deliveriesRate(number_of_deliveries: int):
        if number_of_deliveries < 50:
            return number_of_deliveries * 160
        if 60 > number_of_deliveries >= 50:
            return number_of_deliveries * 200
