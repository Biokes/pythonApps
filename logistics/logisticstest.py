from apps.logistics.dispatch import Dispatch


class LogisticTest:

    def test_number_of_deliveries_payCut_isCalculated(self):
        dispatch: Dispatch = Dispatch()

        assert 0 == dispatch.deliveriesSum(0)
