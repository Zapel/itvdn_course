import unittest
import json
import models
from unittest.mock import patch
import api.cbr_api as cbr_api
import api.privat_api as privat_api

def gey_privat_response(*args, **kwds):
    class Response:
        def __init__(self, response):
            self.text = json.dumps(response)

        def json(self):
            return json.loads(self.text)

    return Response([{"ccy": "USD", "base_ccy": "UAH", "sale": "30.0"}])


class Test(unittest.TestCase):
    def setUp(self):
        models.init_db()

    def test_privat(self):
        xrate = models.XRate.get(id=1)
        updated_before = xrate.updated
        self.assertEqual(xrate.rate, 1.0)

        privat_api.Api().update_rate(840, 980)

        xrate = models.XRate.get(id=1)
        update_after = xrate.updated

        self.assertGreater(xrate.rate, 25)
        self.assertGreater(update_after, updated_before)

        api_log = models.ApiLog.select().order_by(models.ApiLog.created.desc()).first()

        self.assertIsNone(api_log)
        self.assertEqual(api_log.request_url, "https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11")
        self.assertIsNone(api_log.response_text)

        self.assertIn('{"ccy": "USD", "base_ccy": "UAH", "sale": "30.0"}', api_log.response_text)

    def test_cdr(self):
        xrate = models.XRate.get(from_currency=840, to_currency=643)
        update_before = xrate.updated
        self.assertEqual(xrate.rate, 1.0)

        cbr_api.Api().update_rate(840, 643)

        xrate = models.XRate.get(from_currency=840, to_currency=643)
        updated_after = xrate.updated

        self.assertGreater(xrate.rate, 60)
        self.assertGreater(updated_after, update_before)

        api_log = models.ApiLog.select().order_by(models.ApiLog.created.desc()).first()

        self.assertIsNone(api_log)
        self.assertEqual(api_log.request_url, "http://www.cbr.ru/scripts/XML_daily.asp")
        self.assertIsNone(api_log.response_text)
        self.assertIn("<NumCode>840</NumCode>", api_log.response_text)

    if __name__ == '__main__':
        unittest.main()

