#!/usr/bin/python3
from pprint import pprint
from brownie import RWAConsumer, config, network
from scripts.helpful_scripts import fund_with_link, get_account


def main():
    rwa_contract = RWAConsumer[-1]
    print("Request data:")
    print(rwa_contract.data())
    print("Request done")
