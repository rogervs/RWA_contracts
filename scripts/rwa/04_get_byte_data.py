#!/usr/bin/python3
from pprint import pprint
from brownie import RWAConsumer, config, network
from scripts.helpful_scripts import fund_with_link, get_account


def pline(words=""):
    print(
        "================================================================================"
    )
    if words is not "":
        print(words)
        print(
            "================================================================================"
        )


def main():
    account = get_account()
    rwa_contract = RWAConsumer[-1]
    pline("Funding contract with link")
    tx = fund_with_link(
        rwa_contract.address, amount=config["networks"][network.show_active()]["fee"]
    )
    tx.wait(1)
    pline("funding complete")
    pline("Request data:")
    request_tx = rwa_contract.requestBytes("Demo Project A", {"from": account})
    pline("Request done")
    print(request_tx.events)
