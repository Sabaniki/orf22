#!//usr/local/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import csv

# csv format: [from_ip,dest_ip,rtt(ms)]


def read_rtt(file_path):
    prefix = "./test/"
    # prefix = "/csv/"
    file_path = prefix + file_path + ".csv"
    csv_rows = []
    with open(file_path) as f:
        reader = csv.reader(f)
        csv_rows = [row for row in reader]
    rtts = []
    for row in csv_rows:
        rtts.append(int(row[2]))
    return rtts
    
def calc_cdf(rtts):
    rtts = np.array(rtts)
    rtts_count, rtts_bins_count = np.histogram(rtts, bins=rtts.size)
    cdf = np.cumsum(rtts_count / sum(rtts_count))
    return cdf, rtts_bins_count
    
cns_rtts = read_rtt("cns")
print(f"cns: {cns_rtts}")
cns_cdf, cns_bins_count = calc_cdf(cns_rtts)

starlink_rtts = read_rtt("starlink")
print(f"starlink: {starlink_rtts}")
starlink_cdf, starlink_bins_count = calc_cdf(starlink_rtts)


five_g_rtts = read_rtt("five-g")
print(f"5G: {five_g_rtts}")
five_g_cdf, five_g_bins_count = calc_cdf(five_g_rtts)

fig = plt.figure(figsize=(6,4))
ax = plt.subplot(111, xlabel="TCP RTT(ms)", ylabel="CDF")

ax.plot(cns_bins_count[1:], cns_cdf,label="CNS")
ax.plot(starlink_bins_count[1:], starlink_cdf,label="Starlink", linestyle="dashed")
ax.plot(five_g_bins_count[1:], five_g_cdf,label="5G", linestyle="dashed")


plt.legend(loc='upper left', fontsize=11.5, fancybox=False, edgecolor='black')
plt.savefig("/csv/cdf.svg")