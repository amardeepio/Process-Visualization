import psutil
import matplotlib.pyplot as plt


nice = psutil.cpu_times().nice
system=psutil.cpu_times().system
user=psutil.cpu_times().user
idle=psutil.cpu_times().idle

plt.figure(figsize=(5,5))

x=[nice,system,user,idle]

labels=["cpu used by Nice", "cpu used by System","cpu used by user","cpu used by idle"]

explode=(0,0,0,0.1)

plt.pie(x,explode=explode,labels=labels,shadow=True,autopct='%1.1f%%')

plt.title("CPU usage distrution Pie Chart")

plt.show()

print(nice)
print(user)
print(system)
print(idle)




