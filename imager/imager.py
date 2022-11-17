import numpy as np
import matplotlib.pyplot as plt
import csv

# csv format: [from_ip,dest_ip,rtt(ms)]

cns = []
with open(f"./cns.csv") as f:
    reader = csv.reader(f)
    tmp = [row for row in reader]
    cns.append(tmp[2])

starlink = []
with open(f"./starlink.csv") as f:
    reader = csv.reader(f)
    tmp = [row for row in reader]
    starlink.append(tmp[2])

cns = np.array(cns)
starlink = np.array(starlink)

cns_count, cns_bins_count = np.histogram(cns, bins=cns.size)
starlink_count, starlink_bins_count = np.histogram(starlink, bins=starlink.size)

cns_cdf = np.cumsum(cns_count / sum(cns_count))
starlink_cdf = np.cumsum(starlink_count / sum(starlink_count))

fig = plt.figure(figsize=(6,4))
ax = plt.subplot(111, xlabel="TCP RTT(ms)", ylabel="CDF")

ax.plot(cns_bins_count[1:], cns_cdf,label="CNS")
ax.plot(starlink_bins_count[1:], starlink_cdf,label="Starlink", linestyle="dashed")


plt.legend(loc='upper left', fontsize=11.5, fancybox=False, edgecolor='black')
plt.savefig("rtt.png")