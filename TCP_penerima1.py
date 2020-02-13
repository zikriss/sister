import socket

print("kita mau buat tcp penerima socket")
print("langkah 1 : socket")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#sock_stream adalah inisialisasi TCP

print("langkah 2 : bind")
alamat_ip = "localhost"
#alamat_ip = "10.20.192.204"
port_number = 22222
alamat_penerima = (alamat_ip, port_number)
sock.bind(alamat_penerima)
print("langkah 3 : listen")
sock.listen(1)
print("langkah 4 : accept")
print("sedang menunggu koneksi ...")
conn, alamat_pengirim = sock.accept()
print("langkah 5  : menerima")
print("sedang menunggu data kiriman ...")
data = conn.recv(1024)
print("telah diterima : ",data.decode(),"dari : ")
print(alamat_pengirim)
print("langkah 6 : tutup koneksi")
conn.close()