from logistics import Logistics


class TestDispatchCalculator:

    def test_deliveriesAmountOIsCalculated(self):
        assert 13000 == Logistics.calculateWage(50)
        assert Logistics.calculateWage(1) == 5160
