import psutil
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation




cpu_percent =psutil.cpu_percent(interval=0.0, percpu=False)
mem_percent =psutil.virtual_memory().free
mem_percent_active =psutil.virtual_memory().active
mem_percent_avil =psutil.virtual_memory().available

print(type(cpu_percent))
print(type(mem_percent))


print(cpu_percent)
print(mem_percent)
print(mem_percent_active)
print(mem_percent_avil)


plt.figure(figsize=(3,3))

x = [mem_percent,mem_percent_active,mem_percent_avil]

labels =["free memory","active memory","avilable memory"]

plt.pie(x,labels=labels)

plt.show()