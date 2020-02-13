import requests

url = "http://localhost:1880/kelas-post"
payload = "samlekum"
r = requests.post(url, data=payload)
print(r)
print(r.text)