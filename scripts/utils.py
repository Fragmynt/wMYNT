from brownie import accounts, config,  network


def get_account(num =0 ):
    if network.show_active() == "development":
        return accounts[num]
    if network.show_active() == "fragmynt-main":
        return accounts.add(config['wallets']['MAINNET_DEPLOYER'])
    else:
        if num == 0:
            return  accounts.add(config['wallets']['DEPLOYMENT_PRIVATE'])
        elif num == 1:
            return accounts.add(config['wallets']['OWNER_PRIVATE'])
        else:
            raise Exception('Wallet not available')

    