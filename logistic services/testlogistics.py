from logistics import Logistics


class TestDispatchCalculator:

    def test_deliveriesAmountOIsCalculated(self):
        logistics: Logistics = Logistics()
        assert 900 == logistics.calculateWage(50)
