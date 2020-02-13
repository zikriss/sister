import socket

print("kita hendak membuat udp socket pengirim")

print("langkah 1 : membuat socket")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("langkah 2 : tidak perlu binding")

print("langkah 2 : melakukan pengiriman")

alamat_ip = "localhost"

port_number = 65432

alamat_penerima = (alamat_ip, port_number)

data = "samlekum"

sock.sendto(data.encode(), alamat_penerima)

sock.close()