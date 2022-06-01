from brownie import accounts, config,  network


def get_account(num =0 ):
    if network.show_active() == "development":
        return accounts[num]
    else:
        if num == 0:
            return  accounts.add(config['wallets']['DEPLOYMENT_PRIVATE'])
        elif num == 1:
            return accounts.add(config['wallets']['OWNER_PRIVATE'])
        else:
            raise Exception('Wallet not available')

    