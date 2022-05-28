#!/usr/bin/python3
from web3 import Web3
from brownie import RWAConsumer, config, network
from scripts.helpful_scripts import fund_with_link, get_account


def pline(words=""):
    print(
        "================================================================================"
    )
    if words != "":
        print(words)
        print(
            "================================================================================"
        )


def main():
    account = get_account()
    rwa_contract = RWAConsumer[-1]
    oracle_contract = config["networks"][network.show_active()]["oracle"]
    update_tx = rwa_contract.setOracle(oracle_contract, {"from": account})
    pline()
    print(f"Oracle set to {oracle_contract}")
    pline()
