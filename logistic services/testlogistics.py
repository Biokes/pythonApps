from logistics import Logistics


class TestDispatchCalculator:

    def test_deliveriesAmountOIsCalculated(self):
        assert Logistics.calculateWage(1) == 5160
        assert Logistics.calculateWage(0) == 5000
        assert 15000 == Logistics.calculateWage(50)
        assert 16000 == Logistics.calculateWage(55)
        # assert
