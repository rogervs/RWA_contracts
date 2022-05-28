from brownie import MyToken
from web3 import Web3

from scripts.helpful_scripts import (
    get_account,
    BLOCK_CONFIRMATIONS_FOR_VERIFICATION,
)


def deploy_token():
    account = get_account()
    my_token = MyToken.deploy({"from": account})
    my_token.tx.wait(BLOCK_CONFIRMATIONS_FOR_VERIFICATION)
    MyToken.publish_source(my_token)
    return my_token


def main():
    deploy_token()


main()
