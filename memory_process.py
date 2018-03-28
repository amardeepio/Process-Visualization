import psutil

import matplotlib.pyplot as plt

total = psutil.virtual_memory().total
free =psutil.virtual_memory().free
avil=psutil.virtual_memory().available
active=psutil.virtual_memory().active


plt.figure(figsize=(5,5))



y=[total,free,avil,active]

labels=["total memory","total free memory","total available memory","Active memory"]

explode=(0.1,0,0,0.1)

plt.pie(y,explode=explode,labels=labels,shadow=True,autopct='%1.1f%%')

plt.title("Memory usage pie chart")

plt.show()