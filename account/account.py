# Class Account template for each account the user registers
from web3 import Web3
from .aave.aave import Aave

class Account:

    # Set up web3 connection
    def __init__(self, address, web3Instance):
        self.address = address
        self.name = address
        self.web3Instance = web3Instance


    def getBalance(self):
        # Using web3.py
        checksumAddress = self.web3Instance.toChecksumAddress(self.address)
        accountBalance = self.web3Instance.eth.get_balance(checksumAddress)
        convertedAccountBalance = Web3.fromWei(accountBalance, 'ether')
        return convertedAccountBalance

    def depositFundsToAave(self, asset, amount):
        aave = Aave(self.web3Instance)
        txHash = aave.depositToLendingPoolContract(self.address, amount, asset)

    def withdrawFundsFromAave(self):
        # TODO
        pass