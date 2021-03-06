import unittest
import models
import api.cbr_api as cbr_api

class Test(unittest.TestCase):
    def setUp(self):
        models.init_db()

    # def test_main(self):
    #     xrate = models.XRate.get(id=1)
    #     updated_before = xrate.updated
    #     self.assertEqual(xrate.rate, 1.0)
    #     test_api.update_xrates(840, 980)
    #     xrate = models.XRate.get(id=1)
    #     update_after = xrate.updated
    #
    #     self.assertEqual(xrate.rate, 1.01)
    #     self.assertGreater(update_after, updated_before)
    #
    # def test_privat(self):
    #     xrate = models.XRate.get(id=1)
    #     updated_before = xrate.updated
    #     self.assertEqual(xrate.rate, 1.0)
    #     privat_api.update_xrates(840, 980)
    #     xrate = models.XRate.get(id=1)
    #     update_after = xrate.updated
    #
    #     self.assertGreater(xrate.rate, 25)
    #     self.assertGreater(update_after, updated_before)

    def test_cdr(self):
        xrate = models.XRate.get(from_currency=840, to_currency=643)
        update_before = xrate.updated
        self.assertEqual(xrate.rate, 1.0)
        cbr_api.Api().update_rate(840, 643)
        xrate = models.XRate.get(from_currency=840, to_currency=643)
        updated_after = xrate.updated

        self.assertGreater(xrate.rate, 60)
        self.assertGreater(updated_after, update_before)

    if __name__ == '__main__':
        unittest.main()

