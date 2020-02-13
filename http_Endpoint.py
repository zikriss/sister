import requests

url = "http://localhost:1880/kelas-json"
payload = {'nama' : 'namaaaaa', "nim" : 130, 'pesan':'sani'}
r = requests.post(url, json=payload)
print(r)
print(r.text)