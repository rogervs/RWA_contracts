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
    pline("Initiating Audit:")
    request_tx = rwa_contract.initiate_audit(
        "Demo Project A", "audit_admin_a@foxhole", 1000, {"from": account}
    )
    pline("Audit inititated")
