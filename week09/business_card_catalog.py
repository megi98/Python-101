import sqlite3


def add_card(*, id, full_name, email, age, phone, additional_info):
	connection = sqlite3.connect('business_card_catalog.db')
	cursor = connection.cursor()

	insert_querty = f'''
	INSERT INTO User 
	  VALUES({id}, '{full_name}', '{email}', {age}, '{phone}', '{additional_info}');
	'''

	cursor.execute(insert_querty)
	connection.commit()
	connection.close()


def list_all():
	connection = sqlite3.connect('business_card_catalog.db')
	cursor = connection.cursor()

	cursor.execute('SELECT * FROM User;')

	for row in cursor:
		print(f'{row[0]}. ID: {row[0]}, Email: {row[2]}, Full name: {row[1]}\n')

	connection.close()


def get_info(id):
	connection = sqlite3.connect('business_card_catalog.db')
	cursor = connection.cursor()

	cursor.execute('SELECT * FROM User;')

	for row in cursor:
		if row[0] == id:
			print(f'ID: {row[0]}\n')
			print(f'Full name: {row[1]}\n')
			print(f'Email: {row[2]}\n')
			print(f'Age: {row[3]}\n')
			print(f'Phone: {row[4]}\n')
			print(f'Additional info: {row[5]}\n')

	connection.close()


def delete_card(id):
	connection = sqlite3.connect('business_card_catalog.db')
	cursor = connection.cursor()

	cursor.execute(
		f'''
		DELETE FROM User
		  WHERE id={id}
		'''
		)

	connection.commit()
	connection.close()


def help():
	print(
	'''
	#############
	###Options###
	#############

	1. `add` - insert new business card
	2. `list` - list all business cards
	3. `delete` - delete a certain business card (`ID` is required)
	4. `get` - display full information for a certain business card (`ID` is required)
	5. `help` - list all available options
	'''
	)


def main():
	connection = sqlite3.connect('business_card_catalog.db')
	cursor = connection.cursor()

	cursor.execute(
		'''
		CREATE TABLE User(
		  id INTEGER PRIMARY KEY,
		  full_name VARCHAR(50),
		  email VARCHAR(60),
		  age INTEGER,
		  phone VARCHAR(20),
		  additional_info TEXT
		);
		'''
		)

	connection.commit()
	connection.close()
	

if __name__ == '__main__':
	main()