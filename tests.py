import unittest
from format_price import format_price


class TestPrice(unittest.TestCase):
    def test_correct_price(self):
        price = format_price("2345.2312")
        self.assertEqual(price, "2 345.23")

    def test_letters_in_price(self):
        price = format_price("23.as")
        self.assertIsNone(price)

    def test_punctuation_in_price(self):
        price = format_price("45-^5s")
        self.assertIsNone(price)

    def test_none_or_zero_fractial_part(self):
        price1 = format_price(12323211.)
        price2 = format_price(4595.00000)
        self.assertEqual(price1, "12 323 211")
        self.assertEqual(price2, "4 595")

    def test_price_without_dot(self):
        price = format_price(9362262)
        self.assertEqual(price, "9 362 262")

    def test_dots_in_price(self):
        price = format_price("23.453.12.66")
        self.assertIsNone(price)

    def test_none(self):
        price = format_price(None)
        self.assertIsNone(price)
        
    def test_bool(self):
        price = format_price(True)
        self.assertIsNone(price)


if __name__ == "__main__":
    unittest.main()
