import pytest

from apps.class_examples.invalidnumbererror import InvalidNumberError
from logistics import Logistics


class TestDispatchCalculator:

    def test_deliveriesAmountOIsCalculated(self):
        assert Logistics.calculateWage(1) == 5160
        assert Logistics.calculateWage(0) == 5000
        assert 15000 == Logistics.calculateWage(50)
        assert 16000 == Logistics.calculateWage(55)
        assert Logistics.calculateWage(61) == 20250
        assert Logistics.calculateWage(70) == 40000

    def test_invalidDeliveries_raiseError(self):
        with pytest.raises(InvalidNumberError):
            Logistics.calculateWage(-1)
        with pytest.raises(InvalidNumberError):
            Logistics.calculateWage(1000)
