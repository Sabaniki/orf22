use pnet::packet::ethernet::{EtherTypes,EthernetPacket, EtherType};
use pnet::packet::vlan::VlanPacket;
use pnet::packet::Packet;
use crate::handler::ip::v4_handler;
use crate::handler::ip::v6_handler;
use crate::packet::tuples::FiveTupleWithFlagsAndTime;

// Ether のペイロードから IPv4 パケットを抽出．次のレイヤのハンドラを呼び出す
pub fn vlan_handler(ethernet: &EthernetPacket) -> Option<FiveTupleWithFlagsAndTime> {
    if let Some(vlan) = VlanPacket::new(ethernet.payload()) {
        debug!("vlan id: {}", vlan.get_vlan_identifier());
        return call_ip_handler(&vlan, vlan.get_ethertype());
    }
    None
}

pub fn call_ip_handler(frame: &VlanPacket ,next: EtherType) -> Option<FiveTupleWithFlagsAndTime> {
    let frame = EthernetPacket::new(frame.payload()).unwrap();
    match next {
        EtherTypes::Ipv4 => {
            v4_handler(&frame)
        },
        EtherTypes::Ipv6 => {
            v6_handler(&frame)
        },
        _ => {
            None
        }
    }
}