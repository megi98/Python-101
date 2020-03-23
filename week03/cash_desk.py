class Bill:

	def __init__(self, amount):

		if type(amount) is not int:
			raise TypeError("Wrong type!")

		if amount < 0:
			raise ValueError("Negative amount!")

		self.amount = amount


	def __str__(self):

		return f'A {self.amount}$ bill'


	def __repr__(self):

		return f'A {self.amount}$ bill'


	def __int__(self):

		return self.amount


	def __eq__(self, other):

		return self.amount == other.amount


	def __hash__(self):

		return hash(self.amount)


	def __lt__(self, other):

		return self.amount < other.amount



class BillBatch:

	def __init__(self, bills):

		for bill in bills:

			if type(bill) is not Bill:
				raise TypeError('Wrong type!')

		self.bills = bills


	def __repr__(self):

		return f'{self.bills} batches'


	def __str__(self):

		return f'{self.bills} batches'


	def __len__(self):

		return len(self.bills)


	def __getitem__(self, index):

		return self.bills[index]


	def total(self):

		total_amount = 0

		for bill in self.bills:
			total_amount += int(bill)

		return total_amount



class CashDesk:

	__money = 0
	__money_holder = {}

	def take_money(self, money):

		if type(money) is not Bill and type(money) is not BillBatch:		
			raise ValueError("Wrong type!")

		if type(money) is Bill:

			self.__money += int(money)

			if money in self.__money_holder:
				self.__money_holder[money] += 1

			else:
				self.__money_holder[money] = 1

		if type(money) is BillBatch:

			self.__money += money.total()

			for bill in money:

				if bill in self.__money_holder:
					self.__money_holder[bill] += 1
				else:
					self.__money_holder[bill] = 1


	def total(self):
		
		return self.__money


	def inspect(self):

		for key in sorted(self.__money_holder.keys()):
			print("%s - %s" % (f'{int(key)}$ bills', self.__money_holder[key]))



