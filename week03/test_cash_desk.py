import unittest
from cash_desk import (Bill, BillBatch, CashDesk)

class TestBill(unittest.TestCase):

	def test_if_amount_type_is_correct(self):

		amount = 'string'
		exc = None

		try:
			Bill(amount)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Wrong type!')


	def test_if_amount_is_negative(self):

		amount = -20
		exc = None

		try:
			Bill(amount)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Negative amount!')


	def test_string_representation(self):

		bill = Bill(10)

		result = str(bill)
		expected = 'A 10$ bill'

		self.assertEqual(result, expected)



class TestBillBatch(unittest.TestCase):

	def test_bills_type(self):

		bills = [Bill(10), Bill(20), 30]
		exc = None

		try:
			BillBatch(bills)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Wrong type!')


	def test_total(self):

		bills = [Bill(10), Bill(30), Bill(15), Bill(5)]
		batch = BillBatch(bills)

		result = batch.total()

		self.assertEqual(result, 60)



class TestCashDesk(unittest.TestCase):

	def test_take_money_type(self):

		desk = CashDesk()
		exc = None

		try:
			desk.take_money(10)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Wrong type!')


	def test_total(self):

		values = [10, 20, 50, 100, 100, 100]
		bills = [Bill(value) for value in values]
		batch = BillBatch(bills)
		desk = CashDesk()

		desk.take_money(batch)
		desk.take_money(Bill(10))
		total = desk.total()

		self.assertEqual(total, 390)


	
if __name__ == '__main__':
	unittest.main()