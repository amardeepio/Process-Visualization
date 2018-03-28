import psutil
import matplotlib.pyplot as plt 
import numpy as numpy

process =psutil.pids()

print(process)


pr= psutil.cpu_percent(interval=0,percpu=True)


print(pr)



cpu_usage_percent =psutil.cpu_percent(interval=0,percpu=True)

print(cpu_usage_percent)

num_bins = 18
plt.plot(pr,cpu_usage_percent)

n,bins,patches =plt.hist(process,num_bins,facecolor='blue',alpha=0.9)

plt.xlabel("number of processes ")

plt.ylabel("CPU usage")

plt.title ("process histogram")

plt.show()