FROM rust as builder
WORKDIR /workspace
COPY Cargo.lock Cargo.lock
COPY Cargo.toml Cargo.toml
COPY src/ src/
USER 1000:1000
# RUN cargo build --release
RUN cargo build
FROM ubuntu:latest
RUN apt-get update && apt-get install -y jq iproute2 sudo
# COPY --from=builder /workspace/target/release/passive_rtt /passive_rtt
COPY --from=builder /workspace/target/debug/passive_rtt /passive_rtt

ENTRYPOINT tail -f