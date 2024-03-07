from logistics import Logistics


class TestDispatchCalculator:

    def test_deliveriesAmountOIsCalculated(self):
        logistics: Logistics = Logistics()
        assert 13000 == Logistics.calculateWage(50)
