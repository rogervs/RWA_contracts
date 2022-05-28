from brownie import MyToken
from web3 import Web3

from scripts.helpful_scripts import get_account, BLOCK_CONFIRMATIONS_FOR_VERIFICATION


def get_token_balance(account_address):
    my_token = MyToken[-1]
    balance = my_token.balanceOf(account_address)
    print(f"The account {account_address} has balance {balance}")


def send_token(receiver, amount):
    my_token = MyToken[-1]
    my_token.transfer(receiver, amount)
    get_token_balance(receiver)


def main():
    get_token_balance(get_account())
