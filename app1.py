from telethon import TelegramClient, sync

if __name__ == "__main__":
	api_id = 465745
	api_hash = ''

	with open('1.txt', "r") as f:
		lines = f.readlines()

	client = TelegramClient('session_name', api_id, api_hash)
	client.start()

	for record in lines:
		try:
			contact_info = client.get_entity(record)
			a = contact_info.first_name
			b = contact_info.last_name
			c = contact_info.username
			print ('Имя',a)
			print ('Фамилия',b)
			print ('Логин',c)
		except ValueError:
			print('Данные по номеру не найдены.')
			continue