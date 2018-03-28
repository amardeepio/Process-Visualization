import psutil
import matplotlib.pyplot as plt 
import numpy as numpy



disk_usage = int(psutil.disk_usage('/').used)
disk_free =int(psutil.disk_usage('/').free)
disk_total =int(psutil.disk_usage('/').total)




plt.figure(figsize=(3,3))


x=[disk_total,disk_usage,disk_free]

labels=["total space","used space","avilable space"]

explode = (0, 0.1, 0) 



plt.pie(x, explode=explode,labels=labels,shadow=True,autopct='%1.1f%%')



plt.title("Disk usage pie chart")

plt.show()


print(disk_usage)

print(disk_free)

print(disk_total)