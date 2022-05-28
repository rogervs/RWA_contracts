#!/usr/bin/python3
from pprint import pprint
from brownie import RWAConsumer, config, network
from scripts.helpful_scripts import fund_with_link, get_account


def main():
    account = get_account()
    rwa_contract = RWAConsumer[-1]
    tx = fund_with_link(
        rwa_contract.address, amount=config["networks"][network.show_active()]["fee"]
    )
    tx.wait(1)
    print("funding complete")
    print("Initiating Data Conversion:")
    return rwa_contract.bytesToArrays({"from": account})
