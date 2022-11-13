use clap::{ArgMatches, App, Arg};
use anyhow::Context;

fn create_app() -> ArgMatches {
    App::new("passive rtt measurement")
        .version("1.0.0")
        .author("sabaniki")
        .about("this is passive rtt mesuarement application written in Rust.")
        .arg(
            Arg::new("interface_name")
                .value_name("interface_name")
                .index(1)
                .required(true),
        )
        .arg(
            Arg::new("ipv4_range")
                .value_name("ipv4_range")
                .index(2)
                .required(true),
        )
        .arg(
            Arg::new("ipv6_range")
                .value_name("ipv6_range")
                .index(3)
                .required(true),
        )
        .get_matches()
}

pub fn get_arg() -> Result<(String, String, String), anyhow::Error> {
    let app = create_app();
    let interface_name = app.value_of("interface_name")
        .with_context(||"could not get the arg [interface_name]")?;
    let ipv4_range = app.value_of("ipv4_range")
        .with_context(||"could not get the arg [ipv4_range]")?;
    let ipv6_range = app.value_of("ipv6_range")
        .with_context(||"could not get the arg [ipv6_range]")?;
    Ok((interface_name.to_string(), ipv4_range.to_string(), ipv6_range.to_string()))
}
