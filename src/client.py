from src.json_payload import create_identifier_payload
from src.json_payload import create_msg_payload

import requests


def send_payload(first_time=True):
	server_url = 'http://127.0.0.1:8000'
	server_response = requests.get(server_url)
	if server_response.ok:
		print("Server is up and running!")
		if first_time:
			http_payload = create_identifier_payload()
		else:
			http_payload = create_msg_payload()	

		client_post = requests.post(server_url,http_payload)
		if client_post.ok:
			print("server received msg!")
		else:
			print("send again!")	

	else:
		print("No connection!")


send_payload()	
send_payload(first_time=False)	

