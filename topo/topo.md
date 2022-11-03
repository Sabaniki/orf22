# ORF 2022 Test Topology

![topology](./topo.svg)

## Topology
- Client1
    - ORF attendee's device
    - ubuntu
    - access the Internet via normal router
    - access vlan 100

- Client2
    - ORF attendee's device
    - ubuntu
    - access the Internet via Starlink
    - access vlan 200

- AP
    - Wi-Fi Access Point
    - ovs
    - downlink
        - access vlan 100 for Client1
        - access vlan 200 for Client2
    - uplink
        - tag vlan 100, 200

- SW
    - L2 forwarder
    - 

- RTTTer
    - Calculate RTT
        - Run sabaniki implementation
    - ubuntu
    - tag vlan 100, 200
        - 
