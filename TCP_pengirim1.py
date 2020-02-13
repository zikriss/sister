import socket
import json
print("kita membuat socket tcp pengirim")
print("langkah 1 :  membuat socket")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("langkah 2 : koneksi")
alamat_ip = "192.168.43.39"
#alamat_ip = "10.20.192.204"
#alamat_ip = "localhost"
port_number = 22222
alamat_penerima = (alamat_ip, port_number)
sock.connect(alamat_penerima)
while True :

    print("langkah 3 : pengirim")
    data = json.dumps({'nama': "raldrin", 'nim' : "sekian", 'pesan' : "saya wibu garis keras"})
    for i in range(3) :
        sock.send(data.encode())
    print(json.loads(data))
    print("telah terkirim : ", data, "ke alamat : ")
    print(alamat_penerima)
    print("langkah 4 : tutup socket")
    #sock.close()
    x = input()