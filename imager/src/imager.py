#!//usr/local/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import csv

# csv format: [from_ip,dest_ip,rtt(ms)]


def read_rtt(file_path):
    # prefix = "./test/"
    prefix = "/csv/"
    file_path = prefix + file_path + ".csv"
    csv_rows = []
    with open(file_path) as f:
        reader = csv.reader(f)
        csv_rows = [row for row in reader]
    rtts = []
    for row in csv_rows:
        rtts.append(int(row[2]))
    return rtts
    
    
cns_rtts = read_rtt("cns")
print(f"cns: {cns_rtts}")

starlink_rtts = read_rtt("starlink")
print(f"starlink: {starlink_rtts}")



cns = np.array(cns_rtts)
starlink = np.array(starlink_rtts)

cns_count, cns_bins_count = np.histogram(cns, bins=cns.size)
starlink_count, starlink_bins_count = np.histogram(starlink, bins=starlink.size)

cns_cdf = np.cumsum(cns_count / sum(cns_count))
starlink_cdf = np.cumsum(starlink_count / sum(starlink_count))

fig = plt.figure(figsize=(6,4))
ax = plt.subplot(111, xlabel="TCP RTT(ms)", ylabel="CDF")

ax.plot(cns_bins_count[1:], cns_cdf,label="CNS")
ax.plot(starlink_bins_count[1:], starlink_cdf,label="Starlink", linestyle="dashed")


plt.legend(loc='upper left', fontsize=11.5, fancybox=False, edgecolor='black')
plt.savefig("/csv/cdf.svg")