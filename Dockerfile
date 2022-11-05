FROM rust as builder
WORKDIR /workspace
COPY Cargo.lock Cargo.lock
COPY Cargo.toml Cargo.toml
COPY src/ src/
RUN cargo build --release
FROM ubuntu:latest
RUN apt-get update && apt-get install -y jq iproute2 sudo
COPY --from=builder /workspace/target/release/passive_rtt /passive_rtt

ENTRYPOINT tail -f