import socket

print("kita butuh bikin udp socket penerima")
print("langkah 1 : buat socket")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("langkah 2 : melakukan bind")

alamat_ip = "localhost"

port_number = 65432

alamat_penerima = (alamat_ip, port_number)

sock.bind(alamat_penerima)

print("langkah 3 : melakukan receive")
print("sedang menunggu kiriman ...")

data, alamat_pengirim = sock.recvfrom(1024)

print("sudah sampai : ", data.decode(), "dari",)
print(alamat_pengirim)

sock.close()