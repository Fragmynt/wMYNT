from scripts.utils import get_account
from brownie import WETH10


def deploy_wMYNT():
    deployer = get_account(0)
    WETH10.deploy({'from': deployer})


def main():
    deploy_wMYNT()
    pass