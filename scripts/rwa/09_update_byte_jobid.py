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
    conclude_audit_jobId = config["networks"][network.show_active()][
        "conclude_audit_jobId"
    ]
    update_tx = rwa_contract.set_get_byte_JobId(
        Web3.toHex(text=conclude_audit_jobId), {"from": account}
    )
    pline()
    print(f"conclude_audit_jobId set to {conclude_audit_jobId}")
    pline()
