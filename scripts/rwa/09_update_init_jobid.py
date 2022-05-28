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
    init_audit_jobId = config["networks"][network.show_active()]["init_audit_jobId"]
    update_tx = rwa_contract.set_init_audit_JobId(
        Web3.toHex(text=init_audit_jobId), {"from": account}
    )
    pline()
    print(f"init_audit_jobId set to {init_audit_jobId}")
    pline()
