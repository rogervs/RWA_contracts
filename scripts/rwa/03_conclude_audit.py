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
    pline("Concluding Audit:")
    request_tx = rwa_contract.conclude_audit("Project A", {"from": account})
    pline("Audit Concluded")
    print(request_tx.events)
