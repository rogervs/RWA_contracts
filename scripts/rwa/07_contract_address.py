#!/usr/bin/python3
from pprint import pprint
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
    rwa_contract = RWAConsumer[-1]
    pline("Current RWAConsumer Contract Address")
    pline(rwa_contract.address)
