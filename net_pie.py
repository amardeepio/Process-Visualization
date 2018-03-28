import psutil
import matplotlib.pyplot as plt 
import numpy as numpy


net = psutil.net_io_counters()
print(net)

byte_receive = net.bytes_recv
print(byte_receive)


byte_sent=net.bytes_sent
print(byte_sent)


pack_sent = net.packets_sent
print(pack_sent)

pack_rec =net.packets_recv
print(pack_rec)


plt.figure(figsize=(3,3))


x=[byte_sent,byte_receive]

labels =["total bytes sent","total bytes received"]

explode =(0,0.1)

plt.pie(x,explode=explode,labels=labels,shadow=True,autopct='%1.1f%%')

plt.title("Data Traffic Analyze using python")

plt.show()

