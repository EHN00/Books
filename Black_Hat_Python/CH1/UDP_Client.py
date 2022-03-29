import socket

target_host = "8.8.8.8"
target_port = 53

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("After Creation")
#send some Data
client.sendto(b"AAABBBCCC",(target_host,target_port))
print("post Send Data")
#recieve some Data
data, addr = client.recvfrom(4096)
print("I just sent some date")
print(data.decode())
client.close()
