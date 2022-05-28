#!/usr/bin/python3
from brownie import RWAConsumer, config, network
from web3 import Web3
from scripts.helpful_scripts import (
    get_account,
    get_contract,
    BLOCK_CONFIRMATIONS_FOR_VERIFICATION,
)


def deploy_rwa_consumer():
    init_audit_jobId = config["networks"][network.show_active()]["init_audit_jobId"]
    conclude_audit_jobId = config["networks"][network.show_active()][
        "conclude_audit_jobId"
    ]
    get_byte_jobId = config["networks"][network.show_active()]["get_byte_jobId"]

    oracle = config["networks"][network.show_active()]["oracle"]
    fee = config["networks"][network.show_active()]["fee"]
    account = get_account()
    link_token = get_contract("link_token").address
    rwa_consumer = RWAConsumer.deploy(
        oracle,
        Web3.toHex(text=init_audit_jobId),
        Web3.toHex(text=conclude_audit_jobId),
        Web3.toHex(text=get_byte_jobId),
        fee,
        link_token,
        {"from": account},
    )
    if config["networks"][network.show_active()].get("verify", False):
        rwa_consumer.tx.wait(BLOCK_CONFIRMATIONS_FOR_VERIFICATION)
        RWAConsumer.publish_source(rwa_consumer)
    else:
        rwa_consumer.tx.wait(1)
    print(f"RWA Consumer deployed to {rwa_consumer.address}")
    return rwa_consumer


def main():
    deploy_rwa_consumer()


# constructor(address _oracle, bytes32 _init_audit_jobId, bytes32 _conclude_audit_jobId, bytes32 _get_ben_meta_jobId, uint256 _fee, address _link) {
