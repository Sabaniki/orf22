use ipnet::Ipv4Net;
use iprange::IpRange;
use pnet::packet::ethernet::EthernetPacket;
use pnet::packet::ip::{IpNextHeaderProtocols, IpNextHeaderProtocol};
use pnet::packet::ipv4::Ipv4Packet;
use pnet::packet::ipv6::Ipv6Packet;
use pnet::packet::Packet;
use crate::handler::transport::tcp_handler;
use crate::packet::ip::L3Packet;
use crate::packet::tuples::FiveTupleWithFlagsAndTime;

// Ether のペイロードから IPv4 パケットを抽出．次のレイヤのハンドラを呼び出す
pub fn v4_handler(ethernet: &EthernetPacket) -> Option<FiveTupleWithFlagsAndTime> {
    if let Some(packet) = Ipv4Packet::new(ethernet.payload()) {
        let ip_range: IpRange<Ipv4Net> = ["192.168.100.0/24"]
        .iter()
        .map(|s| s.parse().unwrap())
        .collect();
        let src = packet.get_source();
        let dst = packet.get_destination();
        if ip_range.contains(&src) || ip_range.contains(&dst) {
            return call_transport_handler(&packet, packet.get_next_level_protocol());
        }
    }
    None
}

// Ether のペイロードから IPv4 パケットを抽出．次のレイヤのハンドラを呼び出す
pub fn v6_handler(ethernet: &EthernetPacket) -> Option<FiveTupleWithFlagsAndTime> {
    if let Some(packet) = Ipv6Packet::new(ethernet.payload()) {
        let ip_range: IpRange<Ipv4Net> = ["2001:db8:100:200::/64"]
        .iter()
        .map(|s| s.parse().unwrap())
        .collect();
        let src = packet.get_source();
        let dst = packet.get_destination();
        return call_transport_handler(&packet, packet.get_next_header());
    }
    None
}

fn call_transport_handler(packet: &dyn L3Packet ,next: IpNextHeaderProtocol) -> Option<FiveTupleWithFlagsAndTime> {
    match next {
        IpNextHeaderProtocols::Tcp => {
            tcp_handler(packet)
        },
        _ => {
            None
        }
    }
}