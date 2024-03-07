from apps.class_examples.invalidnumbererror import InvalidNumberError


class Logistics:
    @staticmethod
    def calculateWage(deliveries: int):
        if 0 > deliveries or deliveries > 100:
            raise InvalidNumberError
        return Logistics.__deliveriesRate(deliveries) + 5000

    @staticmethod
    def __deliveriesRate(number_of_deliveries: int):
        if number_of_deliveries < 50:
            return number_of_deliveries * 160
        if 60 > number_of_deliveries >= 50:
            return number_of_deliveries * 200
        if 70 > number_of_deliveries >= 60:
            return number_of_deliveries * 250
        if number_of_deliveries >= 70:
            return number_of_deliveries * 500
